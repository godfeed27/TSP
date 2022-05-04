import numpy as np
import pandas as pd
import seaborn as sns
import sys
import os
from matplotlib import pyplot as plt

from app import readParameter


constantDict = readParameter(sys.argv[1])
problemNames = constantDict['PROBLEM_NAMES']
dataInstancesFolder = constantDict['DATA_INSTANCES_FOLDER']
statisticsImageFolder = constantDict['STATISTICS_IMAGE_FOLDER']
# Make folder if not exist
os.makedirs(statisticsImageFolder, exist_ok=True)

statistics = pd.read_json(dataInstancesFolder / 'dataInstances.json', lines=True)
statistics.set_index('name', inplace=True)
statistics = statistics.loc[problemNames, :]


# Plot and save
# Dimension
def classifyDimension(row):
    if row.dimension <= 100:
        return '0 < d <= 100'
    elif row.dimension <= 1000:
        return '100 < d <= 1000'
    else:
        return '1000 < d'


statistics['categoricalDimension'] = statistics.apply(classifyDimension, axis=1)

# Create new figure to plot
plt.figure(1, figsize=(14, 7))

# Plot to countplot
plt.subplot(1, 2, 1)
order = ['0 < d <= 100', '100 < d <= 1000', '1000 < d']
sns.countplot(data=statistics, x='categoricalDimension', orient='v', order=order)
plt.xlabel('Dimension')
plt.ylabel('Number of files')

# plot cumulative density
plt.subplot(1, 2, 2)
x = [0, 100, 1000, 10000, np.inf]
y = [np.sum(statistics['dimension'] <= i) for i in x]
xLabel = [str(element) for element in x]
plt.xlabel('Dimension')
plt.ylabel('Number of files')
plt.plot(xLabel, y)

# Save file
plt.savefig(statisticsImageFolder / 'dimension_statistic.png')

# Optimal Tour
# Create new figure
plt.figure(2, figsize=(14, 7))

# Plot pie chart
plt.subplot(1, 2, 1)
categoricalExistOptimalTour = statistics['existOptimalTour'].value_counts(sort=False)
labels = categoricalExistOptimalTour.keys()
plt.pie(x=categoricalExistOptimalTour, autopct="%.1f%%", explode=[0.01] * len(labels), labels=labels, pctdistance=0.5)
plt.title('Exist Optimal Tour', fontsize=14)
plt.legend(loc='upper right')

# Plot countplot
plt.subplot(1, 2, 2)
sns.countplot(data=statistics, x='existOptimalTour', orient='v')
plt.xlabel('Exist Optimal Tour')
plt.ylabel('Number of files')

# Save file
plt.savefig(statisticsImageFolder / 'existOptimalTour_statistic.png')

# Coordinates
plt.figure(3, figsize=(14, 7))

# Plot pie chart
plt.subplot(1, 2, 1)
categoricalGivenCoordinates = statistics['givenCoordinates'].value_counts(sort=False)
labels = categoricalGivenCoordinates.keys()
plt.pie(x=categoricalGivenCoordinates, autopct='%.1f%%', explode=[0.01] * len(labels), labels=labels, pctdistance=0.5)
plt.title('Given Coordinate', fontsize=14)
plt.legend()

# Plot countplot
plt.subplot(1, 2, 2)
sns.countplot(data=statistics, x='givenCoordinates', orient='v')
plt.xlabel('Exist Coordinates')
plt.ylabel('Number of files')

# Save file
plt.savefig(statisticsImageFolder / 'givenCoordinate_statistic.png')
