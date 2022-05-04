# Greedy

**Greedy algorithms** are algorithms that follow the problem-solving heuristic of making the locally optimal choice at each stage with random start.

## <a name="parameters"></a>Parameters
The Greedy algorithm version in `Greedy.py` requires some parameters below:
- `dataModel`: (`dataModel`) a `dataModel` instance (introduced in [DataModel.md](https://github.com/optimahus/TSP/blob/main/documentation/DataModel.md))
- `timeLimit`: (`int`)time limit for the whole algorithm to solve
- `verbose`: (`int`) a number that decides how much detailed the output should be.

## Code structure
In `Greedy.py`, class `Greedy` has the following methods:

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

- `__findNextCustomer`:

    **Description**\
        Private method that finds the next nearest cumstomer .

    **Parameters**\
    - `candidateCustomers`: (list) list of the remaining customers
    - `currentCustomer`: (int) the index of the current customer

    **Return**\
        An `int` number

- `solve()`:

    **Description**\
        Solves the problem and prints the process based on the `verbose` parameter.

    **Parameters**\
        None.

    **Return**\
        An instance of class `Solution`.