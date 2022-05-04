import sys
import os

from app import readParameter, readTSPLib, setTimeLimit, TSPSolver, readOPTLib


constantDict = readParameter(sys.argv[1])
verbose = constantDict['VERBOSE']
distanceMatricesFolder = constantDict['DISTANCE_MATRICES_FOLDER']
dataFolder = constantDict['DATA_FOLDER']
dateRun = constantDict['DATE_RUN']
optimalResultsFolder = constantDict['OPTIMAL_RESULTS_FOLDER']
outputFolder = constantDict['OUTPUT_FOLDER']
logsFolder = constantDict['LOGS_FOLDER']
# Make folder if not exist
os.makedirs(outputFolder, exist_ok=True)
os.makedirs(logsFolder, exist_ok=True)


for problemName in constantDict['PROBLEM_NAMES']:
    if verbose == 1 or verbose == 2:
        print(f'Solving Problem: {problemName}\n')

    dataModel = readTSPLib(problemName, dataFolder, distanceMatricesFolder)
    dimension = dataModel.dataDescription['DIMENSION']
    timeLimit = setTimeLimit(dimension, constantDict['TIME_LIMIT_OPTIONS'])

    for algoName in constantDict['ALGORITHM_NAMES']:

        solver = TSPSolver(algoName, dataModel, constantDict, timeLimit)
        solution = solver.solve()

        # Check if the  solution if valid. If not, write to log file the errors messages
        solutionErrors = solution.getErrors()
        if solutionErrors:
            logFileName = f'{dateRun}.log'
            logFile = open(logsFolder / logFileName, 'a')

            logFile.write(f'INFOR: ProblemName: {problemName}\n'
                          f'INFOR: AlgorithmName: {solver.comment}\n')

            for error in solutionErrors:
                logFile.write(f'ERROR: {error}\n')
            logFile.write('-----------------------------\n')

        if constantDict['EXPORT_SOLUTION']:
            solution.writeSolution(problemName=problemName, dimension=dimension, algoName=algoName,
                                   executionTime=solver.executionTime,
                                   dateTime=dateRun, comment=solver.comment, outputFolder=outputFolder)
    if verbose == 1 or verbose == 2:
        try:
            optSolution = readOPTLib(problemName, dataFolder, distanceMatricesFolder, optimalResultsFolder)
            print(f'OPT Distance : {optSolution.totalDistance}\n')
        except:
            print(f'OPT Distance : N/A\n')

        print('-----------------------------------------------------------------------------\n')
