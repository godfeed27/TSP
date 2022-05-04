import random
import time
import numpy as np
from itertools import combinations

from .utils import Solution


class Grasp:
    classAbbreviation = 'grasp'

    def __init__(self, dataModel, maxIterations=10, greedinessValue=0.5, timeLimit=1000, verbose=1):
        self.__dataModel = dataModel
        self.__bestSolution = None
        self.__bestFitness = float('Inf')
        self.__size = dataModel.distanceMatrix.shape[0]
        self.__greedinessValue = greedinessValue
        self.__maxIterations = maxIterations
        self.__timeLimit = timeLimit
        self.__verbose = verbose
        self.comment = f'GRASP - maxIterations: {maxIterations} - greedinessValue: {greedinessValue}'

    @classmethod
    def construct(cls, dataModel, constantDict, timeLimit):
        return cls(dataModel, constantDict['MAX_ITERATION'], constantDict['GREEDINESS_VALUE'], timeLimit,
                   constantDict['VERBOSE'])

    def __initialSolution(self, count):
        """
        Return an initial solution using Greedy Randomized algorithm
        """
        if count == 0:
            alpha = 1
        else:
            alpha = self.__greedinessValue
        greedyRandomizedModel = GreedyRandomized(self.__dataModel, alpha)
        solution = greedyRandomizedModel.solve()
        return solution

    def solve(self):
        if self.__verbose == 1 or self.__verbose == 2:
            print(self.comment)

        timeStart = time.time()
        count = 0
        pool = []

        while count < self.__maxIterations:

            timeInterval = time.time() - timeStart
            if timeInterval > self.__timeLimit:
                break

            # Initial Solution
            solution = self.__initialSolution(count)

            # Loop 2-OPT
            localSearchModel = LocalSearch(self.__dataModel, solution)
            currentSolution = localSearchModel.solve(timeStart, self.__timeLimit)

            # Path - relinking
            if count >= 1:
                rand = random.randint(0, len(pool) - 1)
                targetSolution = pool[rand]
                pathRelinkingModel = PathRelinking(self.__dataModel, currentSolution, targetSolution)
                currentSolution = pathRelinkingModel.solve()

            # Compare Fitness Function
            if currentSolution.totalDistance < self.__bestFitness:
                self.__bestSolution = currentSolution
                self.__bestFitness = currentSolution.totalDistance
                pool.append(currentSolution)

            count = count + 1
            if self.__verbose == 2:
                print(f'Iterations = {count: 1d} \tDistance: {self.__bestFitness}')

        if self.__verbose == 1 or self.__verbose == 2:
            print(f'Total Distance: {self.__bestFitness}\n')
        return self.__bestSolution


class GreedyRandomized:
    def __init__(self, dataModel, greedinessValue=0.5):
        self.__distanceMatrix = dataModel.distanceMatrix
        self.__size = self.__distanceMatrix.shape[0]
        self.__greedinessValue = greedinessValue

    def __ranking(self, customer):
        rank = np.zeros((self.__size, 2), dtype=int)
        for i in range(self.__size):
            rank[i, 0] = self.__distanceMatrix[i, customer]
            rank[i, 1] = i
        rank = rank[rank[:, 0].argsort()]
        return rank[:self.__size, 1]

    def solve(self):
        candidateList = [index for index in range(self.__size)]
        customerList = [random.choice(candidateList)]

        for i in range(self.__size):
            count = 0
            rand = random.random()

            if len(customerList) < self.__size:
                if rand <= self.__greedinessValue:
                    nextCustomer = self.__ranking(customerList[-1])[count]
                    while nextCustomer in customerList:
                        count = np.clip(count + 1, 0, self.__size - 1)
                        nextCustomer = self.__ranking(customerList[-1])[count]
                else:
                    nextCustomer = random.choice(candidateList)
                    while nextCustomer in customerList:
                        nextCustomer = random.choice(candidateList)

                customerList.append(nextCustomer)
                candidateList.remove(nextCustomer)

        return Solution(customerList, self.__distanceMatrix)


class LocalSearch:
    def __init__(self, dataModel, solution, loop=20):
        self.__loop = loop
        self.__distanceMatrix = dataModel.distanceMatrix
        self.__size = self.__distanceMatrix.shape[0]
        self.__bestSolution = solution

    def __createNeighborList(self):
        neighborsList = list(combinations(range(self.__size), 2))
        return neighborsList

    def __distanceVariesTwoOpt(self, neighbor, solution):
        customerList = solution.customerList
        maxIdx = max(neighbor)
        minIdx = min(neighbor)
        maxCustomer = customerList[maxIdx]
        minCustomer = customerList[minIdx]
        totalDistanceAfter = 0
        totalDistanceBefore = 0

        if minIdx == maxIdx:
            return 0
        elif minIdx == 0 and maxIdx + 1 == len(customerList):
            return 0
        elif minIdx == 0 and maxIdx + 2 == len(customerList):
            return 0
        elif maxIdx + 1 == len(customerList):
            nextCustomer = customerList[0]
            previousCustomer = customerList[minIdx - 1]
        else:
            nextCustomer = customerList[maxIdx + 1]
            previousCustomer = customerList[minIdx - 1]

        totalDistanceBefore += self.__distanceMatrix[previousCustomer, minCustomer]
        totalDistanceBefore += self.__distanceMatrix[nextCustomer, maxCustomer]

        totalDistanceAfter += self.__distanceMatrix[previousCustomer, maxCustomer]
        totalDistanceAfter += self.__distanceMatrix[nextCustomer, minCustomer]

        totalChange = totalDistanceBefore - totalDistanceAfter
        return totalChange

    @staticmethod
    def swap2Edges(indexNeighborChange, solution, distanceVariesChange):
        minIdx = min(indexNeighborChange)
        maxIdx = max(indexNeighborChange)
        neighborList = solution.customerList
        solution.customerList = neighborList[: minIdx] + neighborList[minIdx: maxIdx + 1][::-1] + neighborList[maxIdx + 1:]
        solution.totalDistance -= distanceVariesChange

    def solve(self, timeStart, timeLimit):
        count = 0
        for i in range(self.__loop):
            if time.time() - timeStart > timeLimit:
                break
            neighborsList = self.__createNeighborList()
            goodNeighbors = [neighbor for neighbor in neighborsList if self.__distanceVariesTwoOpt(neighbor, self.__bestSolution) > 0]
            for goodNeighbor in goodNeighbors:
                distanceVariesChange = self.__distanceVariesTwoOpt(goodNeighbor, self.__bestSolution)
                if distanceVariesChange > 0:
                    count = 0
                    self.swap2Edges(goodNeighbor, self.__bestSolution, distanceVariesChange)
                else:
                    count += 1
            # if count >= 100:
            #     break
        return self.__bestSolution


class PathRelinking:
    def __init__(self, dataModel, startSolution, targetSolution):
        self.__distanceMatrix = dataModel.distanceMatrix
        self.__startSolution = startSolution
        self.__targetSolution = targetSolution
        self.__currentSolution = None
        self.__bestSolution = None

    @staticmethod
    def findSymmetricDifference(startSolution, targetSolution):
        symmetricDifference = []
        for i in range(len(startSolution.customerList)):

            if startSolution.customerList[i] != targetSolution.customerList[i]:
                symmetricDifference.append(i)

        return symmetricDifference

    def __createSolution(self, solution, Idx1, Idx2):
        newCustomerList = solution.customerList.copy()
        newCustomerList[Idx1], newCustomerList[Idx2] = newCustomerList[Idx2], newCustomerList[Idx1]
        return Solution(newCustomerList, self.__distanceMatrix)

    def __move(self, solution, symmetricDifference):
        moveIndex = random.choice(symmetricDifference)
        targetIndex = self.__targetSolution.customerList.index(solution.customerList[moveIndex])
        self.__currentSolution = self.__createSolution(solution, moveIndex, targetIndex)

    def solve(self):
        symmetricDifference = self.findSymmetricDifference(self.__startSolution, self.__targetSolution)

        if self.__startSolution.totalDistance < self.__targetSolution.totalDistance:
            self.__bestSolution = self.__startSolution.__copy__()
        else:
            self.__bestSolution = self.__targetSolution.__copy__()

        self.__currentSolution = self.__startSolution.__copy__()

        while symmetricDifference:
            self.__move(self.__targetSolution, symmetricDifference)
            if self.__currentSolution.totalDistance < self.__bestSolution.totalDistance:
                self.__bestSolution = self.__currentSolution.__copy__()
                
            symmetricDifference = self.findSymmetricDifference(self.__currentSolution, self.__targetSolution)

        return self.__bestSolution
