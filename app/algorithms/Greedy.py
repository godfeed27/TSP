import random
import time

from .utils import Solution


class Greedy:
    classAbbreviation = 'greedy'

    def __init__(self, dataModel, timeLimit, verbose):
        self.__distanceMatrix = dataModel.distanceMatrix
        self.__size = len(dataModel.distanceMatrix)
        self.__timeLimit = timeLimit
        self.__verbose = verbose
        self.comment = 'Greedy'

    @classmethod
    def construct(cls, dataModel, constantDict, timeLimit):
        return cls(dataModel, timeLimit=timeLimit, verbose=constantDict['VERBOSE'])    

    def __findNextCustomer(self, candidateCustomers, currentCustomer):
        minDistance = float('inf')
        nextCustomer = -1
        for customer in candidateCustomers:
            if self.__distanceMatrix[currentCustomer, customer] < minDistance:
                minDistance = self.__distanceMatrix[currentCustomer, customer]
                nextCustomer = customer
        return nextCustomer

    def solve(self):
        # Print the header if verbose = 1 or verbose = 2
        if self.__verbose == 1 or self.__verbose == 2:
            print(self.comment)

        startTime = time.time()

        try:
            customerList = []
            candidateCustomers = [idx for idx in range(self.__size)]
            currentCustomer = random.choice(range(self.__size))
            while candidateCustomers:
                nextCustomer = self.__findNextCustomer(
                    candidateCustomers, currentCustomer)
                customerList.append(nextCustomer)
                candidateCustomers.remove(nextCustomer)
                currentCustomer = nextCustomer

            currentTime = time.time()
            if currentTime - startTime >= self.__timeLimit:
                raise RuntimeError
        except RuntimeError:
            print('Timed out!')

        solution = Solution(customerList, self.__distanceMatrix)

        # Print the final result if verbose = 1 or verbose = 2
        if self.__verbose == 1 or self.__verbose == 2:
            print(f'Total Distance: {solution.totalDistance}\n')
        return solution
