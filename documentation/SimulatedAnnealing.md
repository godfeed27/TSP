# Simulated Annealing

**Simulated Annealing algorithms** are essentially random-search methods in which the new solutions, generated according to a sequence of probability distributions (e.g., the Boltzmann distribution) or a random procedure (e.g., a hit-and-run algorithm), may be accepted even if they do not lead to an improvement in the objective function.

## <a name="parameters"></a>Parameters
The Simulated Annealing version in `SimulatedAnnealing.py` requires some parameters below:
- `dataModel`: (`dataModel`) a `dataModel` instance (introduced in [DataModel.md](https://github.com/optimahus/TSP/blob/main/documentation/DataModel.md))
- `temperature`: (`float`) starting temperature
- `coolingRate`: (`float`) temperature cooldown rate
- `stoppingTemperature`: (`float`) temperature stop condition
- `stoppingIter`: (`int`) inner iteration stop condition
- `times`: (`int`) number of outer loops
- `timeLimit`: (`int`)time limit for the whole algorithm to solve
- `verbose`: (`int`) a number that decides how much detailed the output should be.

## Code structure
In `SimulatedAnnealing.py`, class `SimulatedAnnealing` has the following methods:

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
    - `dataModel`: (`dataModel`) a `dataModel` instance
    - `constantDict`: (`dict`) a parameter dictionary
    - `timeLimit`: (`int`) time limit for the whole algorithm to solve

    **Return**\
        An instance of the class.

- `__initialSolution()`:

    **Description**\
        Private method that generates a starting `Greedy` solution .

    **Parameters**\
        None.

    **Return**\
        An instance of class `Solution`.

- `__accept()`:

    **Description**\
        Private method that considers accepting a candidate.

    **Parameters**\
        `candidate`: (`Solution`) A candidate solution.

    **Return**\
        None.

- `__acceptP()`:

    **Description**\
        Private method that calculates the probability of accepting a candidate.

    **Parameters**\
        `candidateDistance`: (`int`) candidate's total distance.

    **Return**\
        Probability of accepting the candidate.

- `__anneal()`:

    **Description**\
        Private method that performs the main process of the algorithm: finds candidates, calculates the probabilities and updates current best solution.

    **Parameters**\
        `startTime`: (`float`) starting time of the algorithm.

    **Return**\
        None.

- `solve()`:

    **Description**\
        Solves the problem by running multiple loops of annealing and prints the process based on the `verbose` parameter.

    **Parameters**\
        None.

    **Return**\
        An instance of class `Solution`.