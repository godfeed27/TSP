# Genetic Algorithm

**Genetic algorithms** are search methods based on principles of natural selection and genetics.

## <a name="parameters"></a>Parameters
The Genetic Algorithm version in `GeneticAlgorithms.py` requires some parameters below:
- `nodes`: a `dataModel` instance (introduced in [DataModel.md](https://github.com/optimahus/TSP/blob/main/documentation/DataModel.md))
- `popSize`: size of population
- `numGeneration`: number of generation
- `probMutate`: probability of mutation
- `timeLimit`: time limit for the whole algorithm to solve
- `verbose`: a number that decides how much detailed the output should be.

## Code structure
In `GeneticAlgorithms.py`, class `GA` has the following methods:

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

- `__initPopulation()`:

    **Description**\
        Private method that initialize a population.

    **Parameters**\
        None.

    **Return**\
        None.

- `__getDistance()`:

    **Description**\
        Private method that return a distance of a tour.

    **Parameters**\
        `tour`: A solution.

    **Return**\
        `distance`: an integer.

- `__rankBasedSelection()`:

    **Description**\
        Private method that select solution by rank-base.

    **Parameters**\
       None.

    **Return**\
       A solution.

- `__orderBasedCrossover()`:

    **Description**\
        Private method that return a solution by oder-based crossover.

    **Parameters**\
        `parent1`: A solution.
        `parent2`: A solution.

    **Return**\
        `child`: A solution.

- `___mutation()`:

    **Description**\
        Private method that mutate solution.

    **Parameters**\
        `individual`: a solution.

    **Return**\
        None.
- `solve()`:

    **Description**\
        Solves the problem by genetic algorithm.

    **Parameters**\
        None.

    **Return**\
        An instance of class `Solution`.