from numpy import zeros
from random import sample
from time import time

from .Greedy import Greedy


class Tabu:
    classAbbreviation = 'tabu'

    def __init__(self, dataModel, verbose=1, timeLimit=None, neighborSize=3, tabusSize=0.3):
        self.__dataModel = dataModel
        self.__verbose = verbose
        self.__neighborSize = neighborSize
        self.__tabusSize = tabusSize
        self.__bestSolution = None
        self.__timeLimit = timeLimit
        self.comment = f'Tabu - tabusSize: {tabusSize} - neighborSize: {neighborSize}'

    @classmethod
    def construct(cls, dataModel, constantDict, timeLimit):
        return cls(dataModel, constantDict['VERBOSE'], timeLimit,
                   constantDict['NEIGHBOR_SIZE'],
                   constantDict['TABUS_SIZE'],
                   )

    def __initialSolution(self):
        """
        Create initial solution by Greedy if first solution is None.
        """
        solution = Greedy(self.__dataModel, self.__timeLimit, verbose=0).solve()
        self.__bestSolution = solution.__copy__()
        return solution

    def __createNeighborList(self, quantityCustomer):
        """
        Elements of neighbor is pair of customer index .
        """
        return [sample(range(quantityCustomer), k=2)
                for i in range(int(quantityCustomer * self.__neighborSize))]

    def __updateBestSolution(self, solution):
        """
        The best solution corresponds to the current solution.
        """
        self.__bestSolution = solution.__copy__()

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

        totalDistanceBefore += self.__dataModel.distanceMatrix[previousCustomer, minCustomer]
        totalDistanceBefore += self.__dataModel.distanceMatrix[nextCustomer, maxCustomer]
        totalDistanceAfter += self.__dataModel.distanceMatrix[previousCustomer, maxCustomer]
        totalDistanceAfter += self.__dataModel.distanceMatrix[nextCustomer, minCustomer]

        totalChange = totalDistanceBefore - totalDistanceAfter
        return totalChange

    def __swap2Edges(self, indexNeighborChange, solution, distanceVariesChange):
        minIdx = min(indexNeighborChange)
        maxIdx = max(indexNeighborChange)
        neighborList = solution.customerList
        solution.customerList = neighborList[: minIdx] + neighborList[minIdx: maxIdx+1][::-1] + neighborList[maxIdx+1:]
        solution.totalDistance -= distanceVariesChange

    def __checkTabus(self, indexNeighborChange, tabus):
        """
        Check the change is tabu or not by customer index is in tabus or not.
        """
        return indexNeighborChange[0] in tabus and indexNeighborChange[1] in tabus

    def __updateTabus(self, tabus, indexNeighborChange, quantityCustomer):
        """
        Update Tabus by add customer index changed in current solution
        """
        if indexNeighborChange[0] not in tabus:
            customer = indexNeighborChange[0]
        elif indexNeighborChange[1] not in tabus:
            customer = indexNeighborChange[1]
        else:
            return None
        if len(tabus) == round(quantityCustomer * self.__tabusSize):
            tabus.pop(0)
            tabus.append(customer)
        else:
            tabus.append(customer)
    
    def __updateMatrix(self, diversificationMatrix, indexNeighborChange, solution):
        """
        Update matrix every time two customers swap places
        """
        customer1 = solution.customerList[indexNeighborChange[0]]
        customer2 = solution.customerList[indexNeighborChange[1]]
        diversificationMatrix[customer1, customer2] += 1
        diversificationMatrix[customer2, customer1] += 1
        return None

    def __compareToCurrentSol(self, distanceVariesChange):
        return distanceVariesChange >= 0

    def __compareToBestSol(self, solution):
        return solution.totalDistance < self.__bestSolution.totalDistance

    def __localSearch(self, solution, customerQuantity, timeLimit):
        timeStart = time()
        count = 0
        while True:
            neighborsList = self.__createNeighborList(customerQuantity)
            goodNeighbors = [neighbor for neighbor in neighborsList if self.__distanceVariesTwoOpt(neighbor, solution) > 0]

            for goodNeighbor in goodNeighbors:
                distanceVariesChange = self.__distanceVariesTwoOpt(goodNeighbor, solution)
                if distanceVariesChange > 0:
                    count = 0
                    self.__swap2Edges(goodNeighbor, solution,distanceVariesChange)
                    if self.__verbose == 2:
                        print(f'Total Distance of current solution: {solution.totalDistance} '
                              f'(best: {self.__bestSolution.totalDistance})')
                else:
                    count += 1

            timeCheck = time()
            if timeCheck - timeStart > timeLimit:
                return 0
            if count >= 100:
                timeRemaining = timeLimit - (timeCheck - timeStart)
                return timeRemaining

    def __improveSolutions(self, solutionList, customerQuantity, allocateTime):
        timeLeft = (1 - allocateTime) * self.__timeLimit
        solutionList = sorted(solutionList, key=lambda solution: solution.totalDistance)
        while 1:
            for solution in solutionList:
                timeLeft = self.__localSearch(solution, customerQuantity, timeLeft)
            if timeLeft == 0:
                return

    def __compareTwoSolution(self, solution1, solution2):
        return solution1.totalDistance == solution2.totalDistance and solution1.customerList == solution2.customerList

    def __allocateTimeForSections(self, customerQuantity):
        if customerQuantity <= 100:
            allocateTime = 4/5
        elif customerQuantity <= 1000:
            allocateTime = 3/4
        else:
            allocateTime = 1/2
        return allocateTime

    def __mainTabu(self, currentSolution, customerQuantity, tabus, diversificationMatrix, terminationCriteriaStatus):
        neighborsList = self.__createNeighborList(customerQuantity)
        neighborsList = sorted(neighborsList, key=lambda neighbor: (diversificationMatrix[neighbor[0], neighbor[1]],
                               - self.__distanceVariesTwoOpt(neighbor, currentSolution)), reverse=True)
        indexNeighborChange = 0
        distanceVariesChange = 0
        while neighborsList:
            indexNeighborChange = neighborsList[-1]
            distanceVariesChange = self.__distanceVariesTwoOpt(indexNeighborChange, currentSolution)
            neighborsList.pop()
            if self.__compareToCurrentSol(distanceVariesChange):
                self.__swap2Edges(indexNeighborChange,currentSolution, distanceVariesChange)
                self.__updateMatrix(diversificationMatrix, indexNeighborChange, currentSolution)
                if self.__compareToBestSol(currentSolution):
                    self.__updateBestSolution(currentSolution)
                    self.__updateTabus(tabus, indexNeighborChange, customerQuantity)
                    terminationCriteriaStatus = True
                    return terminationCriteriaStatus
                else:
                    self.__updateTabus(tabus, indexNeighborChange, customerQuantity)
                    terminationCriteriaStatus = False
                    return terminationCriteriaStatus
            else:
                if not self.__checkTabus(indexNeighborChange, tabus):
                    self.__swap2Edges(indexNeighborChange, currentSolution, distanceVariesChange)
                    self.__updateMatrix(diversificationMatrix, indexNeighborChange, currentSolution)
                    self.__updateTabus(tabus, indexNeighborChange, customerQuantity)
                    terminationCriteriaStatus = False
                    return terminationCriteriaStatus

        self.__swap2Edges(indexNeighborChange, currentSolution, distanceVariesChange)
        self.__updateMatrix(diversificationMatrix, indexNeighborChange, currentSolution)
        self.__updateTabus(tabus, indexNeighborChange, customerQuantity)
        terminationCriteriaStatus = False
        return terminationCriteriaStatus

    def solve(self):
        if self.__verbose == 1 or self.__verbose == 2:
            print(self.comment)

        timeStart = time()
        tabus = []
        bestSolutionsList = []
        customerQuantity = self.__dataModel.dataDescription['DIMENSION']
        diversificationMatrix = zeros((customerQuantity, customerQuantity))
        currentSolution = self.__initialSolution()
        allocateTime = self.__allocateTimeForSections(customerQuantity)
        terminationCriteriaStatus = False
        lookingLocal = 0

        while True:
            terminationCriteriaStatus = self.__mainTabu(
                currentSolution, customerQuantity, tabus, diversificationMatrix, terminationCriteriaStatus)
            if terminationCriteriaStatus:
                lookingLocal = 0
            else:
                lookingLocal += 1

            if lookingLocal >= (customerQuantity/4):
                temp = [self.__compareTwoSolution(solution, self.__bestSolution) for solution in bestSolutionsList]
                if True not in temp:
                    bestSolutionsList.append(self.__bestSolution.__copy__())
                    lookingLocal = 0

            if self.__verbose == 2:
                print(
                    f'Total Distance of current solution: {currentSolution.totalDistance}')
                print(
                    f'Total Distance of best solution: {self.__bestSolution.totalDistance}')
            timeCheck = time()
            if self.__timeLimit is not None:
                if timeCheck - timeStart > allocateTime * self.__timeLimit:
                    break

        if len(bestSolutionsList) == 0:
            bestSolutionsList.append(self.__bestSolution.__copy__())

        self.__improveSolutions(bestSolutionsList, customerQuantity, allocateTime)
        bestSolution = min(bestSolutionsList, key=lambda solution: solution.totalDistance)
        self.__updateBestSolution(bestSolution)

        if self.__verbose == 1 or self.__verbose == 2:
            print(f'Total Distance of best solution: {self.__bestSolution.totalDistance}\n')

        return self.__bestSolution
