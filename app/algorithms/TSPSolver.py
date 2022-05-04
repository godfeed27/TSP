import time

from .AntColony import ACO
from .GeneticAlgorithms import GA
from .Grasp import Grasp
from .Greedy import Greedy
from .Tabu import Tabu
from .SimulatedAnnealing import SimulatedAnnealing


class TSPSolver:
    def __init__(self, algoName, dataModel, constantDict, timeLimit):
        algoList = [ACO, GA, Grasp, Greedy, SimulatedAnnealing, Tabu]
        self.algorithm = None

        for algo in algoList:
            if algo.classAbbreviation == algoName:
                self.algorithm = algo

        if self.algorithm is None:
            raise ValueError(f'Invalid algoName: {self.algoName}')

        if constantDict['VERBOSE'] > 2:
            raise ValueError(f"Verbose out of range: {constantDict['VERBOSE']}")

        self.dataModel = dataModel
        self.constantDict = constantDict
        self.executionTime = 0
        self.timeLimit = timeLimit

    @property
    def comment(self):
        try:
            return self.model.comment
        except:
            return f'Solve by {self.algorithm.classAbbreviation}'

    def solve(self):
        timeStart = time.time()
        self.model = self.algorithm.construct(self.dataModel, self.constantDict, self.timeLimit)
        solution = self.model.solve()
        self.executionTime = time.time() - timeStart
        return solution
