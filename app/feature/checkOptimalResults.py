import sys
import numpy as np
import pandas as pd

from app import readParameter, readOPTLib


constantDict = readParameter(sys.argv[1])
problemNames = constantDict['PROBLEM_NAMES']
dataInstancesFolder = constantDict['DATA_INSTANCES_FOLDER']
dataFolder = constantDict['DATA_FOLDER']
distanceMatricesFolder = constantDict['DISTANCE_MATRICES_FOLDER']
optimalResultsFolder = constantDict['OPTIMAL_RESULTS_FOLDER']

dataInstances = pd.read_json(dataInstancesFolder / 'dataInstances.json', lines=True)
dataInstances.set_index('name', inplace=True)
dataInstances = dataInstances.loc[problemNames, :]

# Initialize empty list for problem that optimal solution is not reasonable
notReasonable = []

# Loop through each instance (row) to check whether optimal solution is reasonable
for index, row in dataInstances.iterrows():

    # 'existOptimalTour' is true, meaning that this problem is in 'optimalResults' folder
    if row['existOptimalTour']:
        # get name of the problem
        name = index
        # get information about this problem
        informationInstance = readOPTLib(name, dataFolder, distanceMatricesFolder, optimalResultsFolder)
        # get distance of optimal tour
        distance = informationInstance.totalDistance

        # Check
        # bestKnownSolution does not exist, current optimal solution is accepted
        # and move to next iteration
        if row['bestKnownSolution'] is np.nan:
            continue
        # compare distance of current optimal solution to bestKnownSolution
        # and move to next iteration
        elif distance <= row['bestKnownSolution']:
            continue
        # meaning current optimal solution is not optimal
        else:
            notReasonable.append(name)

# Process
if not notReasonable:
    print("All optimal results are reasonable!")
else:
    print(f"The list contains optimal results that are not reasonable: \n{notReasonable}")
