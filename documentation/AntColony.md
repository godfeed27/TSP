# Ant Colony

**Ant Colony algorithms** is a metaheuristic that is inspired by the pheromone trail laying and following behavior of some ant species.

## <a name="parameters"></a>Parameters
The Ant Colony version in `AntColony.py` requires some parameters below:
- `dataModel`: a `dataModel` instance (introduced in [DataModel.md](https://github.com/optimahus/TSP/blob/main/documentation/DataModel.md))
- `colonySize`: size of colony
- `timeLimit`: time limit for the whole algorithm to solve
- `verbose`: a number that decides how much detailed the output should be.

## Code structure
In `AntColony.py`, class `ACO` has the following methods:

- `__init__()`:

    **Description**\
        Class constructor.

    **Parameters**\
        All the parameters in [Parameters](#parameters).

    **Return**\
        None.

- `contruct()`:

    **Description**\
        Class method that returns an instance of the class.

    **Parameters**
    - `dataModel`: a `dataModel` instance
    - `constantDict`: a parameter dictionary
    - `timeLimit`: time limit for the whole algorithm to solve

    **Return**\
        An instance of the class.

- `__selectNode()`:

    **Description**\
        Private method that select unvisited node.

    **Parameters**\
        `ant`: A solution.

    **Return**\
        An integer.

- `__twoOpt()`:

    **Description**\
        Private method that return a better solution.

    **Parameters**\
        `ant`: A solution.

    **Return**\
        `ant`: A solution.

- `__findTour()`:

    **Description**\
        Private method that find tour for an ant.

    **Parameters**\
       `ant`: A solution.

    **Return**\
        None.

- `__addPheromone()`:

    **Description**\
        Private method that add pheromone to tour.

    **Parameters**\
        `ant`: A solution.

    **Return**\
        None.

- `__evaporatePheromone()`:

    **Description**\
        Private method that calculate pheromone evaluation.

    **Parameters**\
        None.

    **Return**\
        None.
- `__MMAS()`:

    **Description**\
        Private method that use MAX-MIN ant system.

    **Parameters**\
        None.

    **Return**\
        An instance of class `Solution`.
- `solve()`:

    **Description**\
        Solves the problem by MAX-MIN ant system.

    **Parameters**\
        None.

    **Return**\
        An instance of class `Solution`.