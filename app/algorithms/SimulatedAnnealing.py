import math
import numpy as np
import random
import time

from .Greedy import Greedy


class SimulatedAnnealing:
    classAbbreviation = 'sa'

    def __init__(self, dataModel, temperature=None, coolingRate=None, stoppingTemperature=None, stoppingIter=None, times=None, timeLimit=None, verbose=None):
        self.__dataModel = dataModel
        self.__temperature = np.amax(self.__dataModel.distanceMatrix) if temperature is None else temperature
        self.__coolingRate = 0.9977 if coolingRate is None else coolingRate
        self.__stoppingTemperature = 1e-8 if stoppingTemperature is None else stoppingTemperature
        self.__stoppingIter = 1000 if stoppingIter is None else stoppingIter
        self.__times = 10000 if times is None else times
        self.__timeLimit = timeLimit
        self.__verbose = 0 if verbose is None else verbose
        self.comment = f'SimulatedAnnealing - temperature: {self.__temperature} - coolingRate: {self.__coolingRate} - '
        self.comment += f'stoppingTemperature: {self.__stoppingTemperature} - stoppingIter: {self.__stoppingIter} - times: {self.__times}'

        self.__initialTemperature = self.__temperature
        self.__bestSolution = None
        self.__bestDistance = float('Inf')
        self.__solutionList = []
        self.__distanceList = []

    @classmethod
    def construct(cls, dataModel, constantDict, timeLimit):
        algoParams = ['TEMPERATURE', 'COOLING_RATE', 'STOPPING_TEMPERATURE', 'STOPPING_ITER', 'TIMES']
        algoDict = {}
        for param in algoParams:
            if param in constantDict.keys():
                algoDict[param] = constantDict[param]
            else:
                algoDict[param] = None

        return cls(dataModel, temperature=algoDict['TEMPERATURE'], coolingRate=algoDict['COOLING_RATE'],
                   stoppingTemperature=algoDict['STOPPING_TEMPERATURE'], stoppingIter=algoDict['STOPPING_ITER'],
                   times=algoDict['TIMES'], timeLimit=timeLimit, verbose=constantDict['VERBOSE'])

    def __initialSolution(self):
        """
        Return an initial solution using Greedy algorithm
        """
        greedyModel = Greedy(self.__dataModel, self.__timeLimit, verbose=0)
        solution = greedyModel.solve()

        # Print all steps when verbose = 2
        if self.__verbose == 2:
            print(f'Greedy Distance: {solution.totalDistance}')

        currentDistance = solution.totalDistance
        if currentDistance < self.__bestDistance:
            self.__bestSolution, self.__bestDistance = solution, currentDistance
        self.__solutionList.append(solution)
        self.__distanceList.append(currentDistance)
        return solution, currentDistance

    def __accept(self, candidate):
        """
        Accept with probability 1 if candidate is better than current.
        Accept with probability __acceptP(..) if candidate is worse.
        """
        candidateDistance = candidate.totalDistance
        if candidateDistance < self.__currentDistance:
            self.__currentDistance, self.__currentSolution = candidateDistance, candidate
            self.__solutionList.append(candidate)
            if candidateDistance < self.__bestDistance:
                self.__bestDistance, self.__bestSolution = candidateDistance, candidate
        else:
            if random.random() < self.__acceptP(candidateDistance):
                self.__currentDistance, self.__currentSolution = candidateDistance, candidate
                self.__solutionList.append(candidate)

    def __acceptP(self, candidateDistance):
        """
        Probability of accepting if the candidate is worse than current.
        Depends on the current temperature and difference between candidate and current.
        """
        return math.exp(-abs(candidateDistance - self.__currentDistance) / self.__temperature)

    def __anneal(self, startTime=None):
        """
        Execute simulated annealing algorithm.
        """
        self.__currentSolution, self.__currentDistance = self.__initialSolution()
        iter = 1
        improvement = 0
        while self.__temperature >= self.__stoppingTemperature and iter < self.__stoppingIter:
            acceptedDiffRatio = 0.05
            acceptedDiff = acceptedDiffRatio * self.__currentDistance
            candidate = self.__currentSolution.getBestNeighbor(acceptedDiff)
            self.__accept(candidate)

            self.__temperature *= self.__coolingRate
            iter += 1
            self.__distanceList.append(self.__currentDistance)

            lastImprovement = improvement
            improvement = 100 * (self.__distanceList[0] - self.__bestDistance) / (self.__distanceList[0])

            # Print all steps when verbose = 2
            if self.__verbose == 2:
                if improvement > lastImprovement:
                    print(f'Total Distance: {self.__bestDistance:8.0f}  Improvement: {improvement:5.2f}%')
            if startTime:
                if time.time() - startTime >= self.__timeLimit:
                    raise RuntimeError

    def solve(self):
        # Print the header if verbose = 1 or verbose = 2
        if self.__verbose == 1 or self.__verbose == 2:
            print(self.comment)

        startTime = time.time()
        try:
            for i in range(1, self.__times + 1):
                # Print all steps when verbose = 2
                if self.__verbose == 2:
                    print(f'Iteration {i}/{self.__times} -------------------------------')
                self.__temperature = self.__initialTemperature
                self.__anneal(startTime=startTime)
                currentTime = time.time()
                if currentTime - startTime >= self.__timeLimit:
                    raise RuntimeError
        except RuntimeError:
            print('Timed out!')

        # Print the final result if verbose = 1 or verbose = 2
        if self.__verbose == 1 or self.__verbose == 2:
            print(f'Total Distance: {self.__bestDistance}\n')
        return self.__bestSolution
