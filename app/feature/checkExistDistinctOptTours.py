import sys
import os

from app import readOPTLib, readParameter, readResultFile, Solution, readTSPLib


constantDict = readParameter(sys.argv[1])
outputFolder = constantDict['OUTPUT_FOLDER']
optimalResultsFolder = constantDict['OPTIMAL_RESULTS_FOLDER']
distanceMatricesFolder = constantDict['DISTANCE_MATRICES_FOLDER']
dataFolder = constantDict['DATA_FOLDER']
dateRun = constantDict['DATE_RUN']
listOptimalProblem = os.listdir(optimalResultsFolder)
# List of files with the same optimal solution
fileList = []
for file in os.listdir(outputFolder):
    fileName = file.split('.')
    problemName = fileName[0]
    algoName = fileName[1]
    if problemName + '.opt.tour' not in listOptimalProblem:
        continue
    else:
        dataDict = readResultFile(problemName, algoName, dateRun, outputFolder)
        dataModel = readTSPLib(problemName, dataFolder, distanceMatricesFolder)
        # Because class Solution get a tour that beginning from 0
        tour = [int(i-1) for i in dataDict['TOUR']]
        solution = Solution(tour, dataModel.distanceMatrix)
        optimalSolution = readOPTLib(problemName, dataFolder, distanceMatricesFolder, optimalResultsFolder)
        if solution.totalDistance != optimalSolution.totalDistance:
            continue
        else:
            if Solution.solutionFormat(solution.customerList) == \
                    Solution.solutionFormat(optimalSolution.customerList):
                continue
            else:
                fileList.append(file)
if fileList:
    print("Files with multiple optimal solutions:")
    for file in fileList:
        print(file)
else:
    print("Don't have file with multiple optimal solutions")
