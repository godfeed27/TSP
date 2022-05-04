# Greedy Randomized Adaptive Search Procedure (GRASP)

**GRASP**  is a metaheuristic algorithm commonly applied to combinatorial optimization problems. GRASP typically consists of iterations made up from successive constructions of a greedy randomized solution and subsequent iterative improvements of it through a local search.


## The GRASP version in `Grasp.py` requires 4 class below:
## 1. GreedyRandomized
### <a name="parameters_greedyRandomized"></a>Parameters
- `dataModel`: a `dataModel` instance (introduced in [DataModel.md](https://github.com/optimahus/TSP/blob/main/documentation/DataModel.md))
- `greedinessValue`: greediness Value in the range [0, 1].

### Code structure
Class `GreedyRamdomized` has the following methods:

- `__init__()`:

    **Description**\
        Class constructor.

    **Parameters**\
        All the parameters in [Parameters](#parameters_greedyRandomized).

    **Return**\
        None.


- `__ranking()`:

    **Description**\
        Private method that evaluate distance from one customer to the rest.

    **Parameters**\
        `customer`:

    **Return**\
        List of customer has been sorted by distance from `customer`
  

- `solve()`:

    **Description**\
        Solves the problem by running multiple loops of greedyRandomized

    **Parameters**\
        None.

    **Return**\
        An instance of class `Solution`.
  
## 2. LocalSearch
### <a name="parameters_localSearch"></a>Parameters
- `dataModel`: a `dataModel` instance (introduced in [DataModel.md](https://github.com/optimahus/TSP/blob/main/documentation/DataModel.md))
- `solution`:  a `Solution` instance (introduced in [Solution.md](https://github.com/optimahus/TSP/blob/main/documentation/Solution.md))
- `loop`: limit iteration of `LocalSearch` (default = 20)

### Code structure
Class `LocalSearch` has the following methods:

- `__init__()`:

    **Description**\
        Class constructor.

    **Parameters**\
        All the parameters in [Parameters](#parameters_localSearch).

    **Return**\
        None.


- `__createNeighborList()`:

    **Description**\
        Private method that make a list of neighbor.

    **Parameters**\
        None.

    **Return**\
        List of neighbor.
  

- `__distanceVariesTwoOpt()`:

    **Description**\
        Private method that find variable distance.

    **Parameters**\
        - `neighbor`:\
        - `solution`: a `Solution` instance

    **Return**\
        Distance change when swap edge.
  

- `swap2Edges()`:\
    **Description**\
        Swap two edge

    **Parameters**\
        - `indexNeighborChange`:\
        - `solution`: a `Solution` instance\
        - `distanceVariesChange`:

    **Return**\
        None
  

- `solve()`:\
    **Description**\
        Improve the solution by running multiple loops of LocalSearch

    **Parameters**\
        - `startTime`:\
        - `limitTime`:
  
    **Return**\
         An instance of class `Solution`.

## 3. PathRelinking
### <a name="parameters_pathRelinking"></a>Parameters
- `dataModel`: a `dataModel` instance (introduced in [DataModel.md](https://github.com/optimahus/TSP/blob/main/documentation/DataModel.md))
- `startSolution`:  a `Solution` instance (introduced in [Solution.md](https://github.com/optimahus/TSP/blob/main/documentation/Solution.md))
- `targetSolution`:  a `Solution` instance

### Code structure
Class `PathRelingking` has the following methods:

- `__init__()`:

    **Description**\
        Class constructor.

    **Parameters**\
        All the parameters in [Parameters](#parameters_pathRelinking).

    **Return**\
        None.


- `findSymmetricDifference()`:

    **Description**\
        Static method that make symmetric difference.

    **Parameters**\
        - `startSolution`:\
        - `targetSolution`:

    **Return**\
        List of neighbor.
  

- `__createSolution()`:

    **Description**\
        Private method that creat a new Solution by swap customer.

    **Parameters**\
        - `solution`: a `Solution` instance\
        - `Idx1`:\
        - `Idx2`: 

    **Return**\
        An instance of class `Solution`.
  

- `__move()`:\
    **Description**\
        Update `currentSolution` by `__creatSolution()`

    **Parameters**\
        - `solution`: a `Solution` instance\
        - `symmetricDifference`:

    **Return**\
        None


- `solve()`:\
    **Description**\
        Improve the solution by PathRelinking

    **Parameters**\
        None.

    **Return**\
         An instance of class `Solution`.

## 4. Grasp
### <a name="parameters"></a>Parameters
- `dataModel`: a `dataModel` instance (introduced in [DataModel.md](https://github.com/optimahus/TSP/blob/main/documentation/DataModel.md))
- `maxIteration`: limit of iteration.
- `greedinessValue`: greediness value in range [0, 1]
- `timeLimit`: time limit for the whole algorithm to solve.
- `verbose`: a number that decides how much detailed the output should be.

### Code structure
Class `Grasp` has the following methods:

- `__init__()`:

    **Description**\
        Class constructor.

    **Parameters**\
        All the parameters in [Parameters](#parameters).

    **Return**\
        None.
  

- `construct()`:
  **Description**\
        Class method that returns an instance of the class.

    **Parameters**\
        - `dataModel`: a `dataModel` instance\
        - `constanDict`: a dictionary contain parameters and values of them\
        - `timeLimit`: time limit for the whole algorithm to solve

    **Return**\
        An instance of class `Solution`.


- `solve()`:

    **Description**\
        Solves the problem by running multiple loops of `GRASP` and prints the process based on the `verbose` parameter.

    **Parameters**\
        None.

    **Return**\
        An instance of class `Solution`.
