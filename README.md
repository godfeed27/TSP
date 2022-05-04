# Traveling Salesman Problems

### Directory Structure

```txt
TSP/
  app/               contains algorithms and features
  data/              contains data instances
  distanceMatrices/  contains distance matrix files
  documentation/     contains documentation for the algorithms
  evaluation/        contains evaluation of algorithms
  logs/              contains log files
  optimalResults/    contains optimal results
  output/            contains exported solution files
  parameters/        contains parameter files
  statistics/        contains statistical analysis of the data instances
```

### Data Description

Data
http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/

Large data
http://www.math.uwaterloo.ca/tsp/world/countries.html

Data description
http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp95.pdf

Data FAQ
http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/TSPFAQ.html

One can download the datasets `.tsp`, `.opt.tsp` from [here](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/ALL_tsp.tar.gz) by:
- For Windows:
    - Install [winrar](https://www.win-rar.com/start.html?&L=10) and set path:
        ```
        set path="path\to\WinRAR\";%path%
        ```
    - Run `getData-Win.bat`:
        ```console
        > getData-Win.bat
        ```
- For Linux/MacOS:
    - Install `curl`:
        ```
        > sudo apt install curl
        ```
    - Run getData-Unix.sh:
        ```
        > bash getData-Unix.sh
        ```

### Instances Description

The file [`dataInstances.json`](https://github.com/optimahus/TSP/blob/main/statistics/instances/dataInstances.json) contains general statistics on some basic information about the problems (or instances):
- `NAME`: name of the problem
- `DIMENSION`: the number of cities in the problem
- `BEST_KNOWN_SOLUTION`: the best value of a solution has been found from all sources (currentely based on `TSPLIB_BestKnownSolution.json` file in `statistic/instances`)
- `EXIST_OPTIMAL_TOUR`: `true` if the optimal tour for the problem has been found and put in `optimalResults` folder, else `false`
- `GIVEN_COORDINATES`: `true` if the problem provides coordinates, else `false`

### Remark on datasets
- The problems whose dimensions are greater than or equal to 10000 are not considered.
- The two problems `lin318.tsp` and `linhp318.tsp` have the same name and data.\
Therefore, the `linhp318.tsp` problem is not considered.
- The problem `dsj1000.tsp` has `CEIL_2D` as its `EDGE_WEIGHT_TYPE`. Meanwhile, the `TSPLIB_BestKnownSolution.json` contains two records of the `dsj1000.tsp` problems: `dsj1000EUC_2D` and `dsj1000CEIL_2D` with `EUC_2D` and `CEIL_2D` as ` EDGE_WEIGHT_TYPE` respectively.\
Therefore, the record `dsj1000EUC_2D` is removed and the record `dsj1000CEIL_2D` is renamed to `dsj1000`.

### References

[Ant Colony Optimization](https://web2.qatar.cmu.edu/~gdicaro/15382/additional/aco-book.pdf)

### Algorithm Abbreviation
| Algorithm        | Abbreviation | Doers |
|:---------------------:|:---------:|---:|
|Ant Colony      | ac |Tran Thanh Tung|
|Genetic Algorithm   | ga |Tran Thanh Tung
| Greedy Randomized Adaptive Search Procedures| grasp| Nguyen Van Quan & Dang Quy Anh |
| Greedy | greedy | Phan Viet Tan |
| Simulated Annealing | sa | Phan Viet Tan & Nguyen Ngoc Hai |
| Tabu Search | tabu | Dang Quang Anh & Cao Viet Tung |

# Installation

***Note: The directory in Linux is different from that in Windows. Therefore, if errors with '/' and '\\' encountered, the path need to be modified.*** 

Example:
- On Linux:	`https://github.com/optimahus`
- On Windows:	`https:\\github.com\optimahus`

## Clone repository
First of all, you need to download the repository. You can either run the script below on the command-line or terminal:

`git clone https://github.com/optimahus/TSP.git`

or download zip file of repository and unzip. 

If you have the problem related to personal access token, try following the steps below:
- Log in to your GitHub account
- Go to `Settings`, then choose `Developer Settings`
- Choose `Personal access tokens`
- Generate and copy your tokens
- Clone again and paste tokens to password space

## Set PYTHONPATH
Add `TSP/` directory pathname to PYTHONPATH.
- For Windows:

  Run command line _as administrator_ and execute the following command:
    ```console
     setx PYTHONPATH "%PYTHONPATH%;\path\to\TSP" /M
    ```
  
  **Note**: 
    * After run this command, you need restart terminal to update PYTHONPATH.
    *  Windows can't set PYTHONPATH for the current terminal session, so this command sets PYTHONPATH permanently.


- For Linux/MacOS:
  ```console
  export PYTHONPATH=$PYTHONPATH:/path/to/TSP
  ```
  
  **Note**: This command only set PYTHONPATH for the current terminal session.

## Change directory
Change the `path` that points to your TSP folder.

```
cd path/to/TSP
```

## Create python virtual environment:
* Create environment by following command:
    ```console
    python3 -m venv env
    ```

* Activate environment:
    ```console
    env/Scripts/activate # For windows
    source env/bin/activate # For Linux or MaxOS
    ```

* Install libraries in by:
  ```console
  pip install -r requirements.txt
  ```

* Deactivate environment:
    ```console
    env/Scripts/deactivate # For windows
    source env/bin/deactivate # For Linux or MaxOS
    ```
      
## Create parameter file
In folder `parameters/`, one has to create parameter files based on the corresponding sample parameter files:
- `TSP_Folder`: path to the TSP directory.
- `PROBLEM_NAMES`: problem names seperated by commas.
- `ALGORITHM_NAMES`: algorithm abbreviations seperated by commas.
- `TIME_LIMIT_OPTIONS`: time limits that depend on the dimensions of the problems.\
For example,  
    ```
    TIME_LIMIT_OPTIONS:100~60|1000~600|10000~600|100000~1200
    ``` 
    is equivalent to:

    | Number of Cities      | Time Limit |
    |:----------------------|-----------------:|
    | 1 <= n <= 100         |           60 s |
    | 100 < n <= 1,000      |          600 s |
    | 1,000 < n <= 10,000   |          600 s |
    | 10,000 < n <= 100,000 |          1200 s |

    **Note**: The last bound's dimension must be greater than the greatest dimension in the problems.
- `DATA_FOLDER`: path to the folder that contains data instances.\
Highly recommend setting `data` as default.
- `DATA_INSTANCES_FOLDER`: path to the folder that contains the statistics of the data instances.\
Highly recommend setting `statistics/instances/` as default.
- `DISTANCE_MATRICES_FOLDER`: path to the folder that contains the distance matrix files.\
Highly recommend setting `distanceMatrices` as default.
- `EVALUATE_IMAGE_FOLDER`: path to the folder that contains the evaluation images.
- `LEADER_BOARD_FOLDER`: path to the folder that contains the algorithms leader board.
- `OPTIMAL_RESULTS_FOLDER`: path to the folder that contains the optimal result files.\
Highly recommend setting `optimalResults` as default.
- `OUTPUT_FOLDER`: path to the output folder.\
Highly recommend setting `output` as default.
- `LOGS_FOLDER`: path to the report folder that contains log files.
- `STATISTICS_IMAGE_FOLDER`: path to the folder that contains the statistical images.
- `EXPORT_SOLUTION`: decides whether the solution is exported or not (`yes` or `no`).
- `DATE_RUN`: date when script was run (format: `yyyymmdd`).
- `VERBOSE`: decides how much detailed the output should be.\
If `VERBOSE` = 0, prints nothing.\
If `VERBOSE` = 1, prints header and final result only.\
If `VERBOSE` = 2, prints the whole algorithm's process.
- Algorithm parameters: parameters' values for the algorithms.

**Note**: Default parameters' values are given in the sample parameters files in the `parameters/` folder.

# Features
## 1. <a name="saveDistanceMatrix"></a>Create distance matrix files
One can generate and save distance matrix files locally by running the following:
```console
python3 app/feature/saveDistanceMatrix.py path/to/parameter.txt
```
The distance matrix files (e.g. `a280.matrix.tsp`) will then be generated and saved in `DISTANCE_MATRICES_FOLDER` (in the parameter file) folder.

## 2. Create json file that stores data information
One can get data instances' information summary in a json file `dataInstances.json` by running the following:
```console
python3 app/feature/getDataInstances.py path/to/parameter.txt
```
The `dataInstances.json` will then be saved in `dataInstances` (in the parameter file) folder.

## 3. Draw statistical analysis
One can get statistical analysis of the problems on dimensions, coordinates and optimal tours by running the following:
```console
python3 app/feature/statisticsPlot.py path/to/parameter.txt
```
The statistical analysis will then be saved in `STATISTICS_IMAGE_FOLDER` (in the parameter file) folder.

## 4. Validate optimal results
One can check if the optimal results are reasonable by running the following:
```console
python3 app/feature/checkOptimalResults.py path/to/parameter.txt
```
The result will then be printed to the output.

## 5. Solve TSP
One can solve the TSP problems using the algorithms above by running the following:
```console
python3 app/feature/problemSolve.py path/to/parameters.txt
```
The results will then be saved in `OUTPUT_FOLDER` (in the parameter file) folder.

**Note**: 
* The distance matrix files should be generated locally beforehand ([feature 1](#saveDistanceMatrix)) for faster performance.
* Rerunning the same parameter file will not guarantee the same solution

## 6. Evaluate results
One can evaluate the results after solving by running the following:
```console
python3 app/feature/evaluateResults.py path/to/parameters.txt
```
The algorithms' results comparison and the leader board for the algorithms will then be saved in `STATISTICS_IMAGE_FOLDER` and `LEADER_BOARD_FOLDER` (in the parameter file) folders , respectively.

## 7. Check distinct optimal tours
In the TSPLIB95 data description, there is a remark:
> There may exist several shortest tours for a problem instance.

One can check if a solution tour with the optimal total distance is different from the optimal tour by running the following:
```console
python3 app/feature/checkExistDistinceOptTours.py path/to/parameters.txt
```
The result will then be printed to the output.# TSP
