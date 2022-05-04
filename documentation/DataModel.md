# Data Models
The classes listed below are defined in `utils.py`.
## 1. Class DataModel

Stores problem's data with `distanceMatrix`, `dataDescription` and `customerArray` (optional):
- `distanceMatrix`: a `numpy.ndarray` instance that contains the distance matrix.
- `dataDescription`: a dictionary that contains the problem's description, such as `NAME`, `TYPE`, `DIMENSION`,...
- `customerArray=None`: a `numpy.ndarray` object that contains customers' coordinates, if it is passed.

This class has 2 methods:
- `__init__()`:

    **Description**\
        Class constructor.

    **Parameters**\
        `distanceMatrix`: (`numpy.ndarray`) the distance matrix.\
        `dataDescription`: (`dict`) the problem's description.\
        `customerArray` (optional): (`numpy.ndarray`) customers' coordinates.

    **Return**\
        None.

- `__repr__()`:

    **Description**\
        Returns a printable representational string of the data model.

    **Parameters**\
        None.

    **Return**\
        A string represents the data model.

## 2. Class Solution
Stores a solution to the problem with `customerList` and `distanceMatrix`:
- `customerList`: a list whose elements are customers' indices in some order.
- `distanceMatrix`: a `numpy.ndarray` instance that contains the distance matrix.

This class has 12 methods:
- `__init__()`:

    **Description**\
        Class constructor.

    **Parameters**\
        `customerList`: (`list`) a list contains customers' indices in some order.\
        `distancematrix`: (`numpy.ndarray`) the distance matrix.

    **Return**\
        None.

- `__repr__()`:

    **Description**\
        Returns a printable representational string of the data model.

    **Parameters**\
        None.

    **Return**\
        A string represents a list of customers.

- `__copy__()`:

    **Description**\
        Return a copy of the class instance.

    **Parameters**\
        None.

    **Return**\
        A class `Solution` instance.

- `__eq__()`:

    **Description**\
        Defines the equality logic for comparing two instances.

    **Parameters**\
        `other`: (`Solution`) the other instance.

    **Return**\
        `True` or `False`.

- `getBestNeighbor()`:

    **Description**\
        Returns the best neighbor found using several search methods.

    **Parameters**\
        `diff`: (`int`) the accepted difference between the worse solution and the current solution.\
        `size=50`: (`int`) number of neighbors considered.

    **Return**\
        A class `Solution` instance.

- `customizedTwoOpt()`:

    **Description**\
        Return a solution by swapping two edges with difference condition

    **Parameters**\
        `diff`: (`int`) the accepted difference between the worse solution and the current solution.

    **Return**\
        A class `Solution` instance.

- `get2EdgesSwapDiff()`:

    **Description**\
        Return the difference after swapping two edges by swapping two nodes (customers).

    **Parameters**\
        `nodeIdx1`: (`int`) index of the first node.\
        `nodeIdx2`: (`int`) index of the second node.

    **Return**\
        An `int` number.

- `insertCustomer()`:

    **Description**\
        Inserts a customer to the `customerList`, default position is the end of the `customerList`.

    **Parameters**\
        `customerIdx`: (`int`) index of the inserted customer.\
        `pos=-1`: (`int`) position index where the customer is inserted.

    **Return**\
        None.

- `solutionFormat()`:

    **Description**\
        Static method that formats and returns the `customerList` to have the customer with index 1 be the start value of the `customerList` and the next customer be the one with the lower index (between the two customers to the left and the right of the customer with index 1) while maintaining the path.

    **Parameters**\
        None.

    **Return**\
        A list of customer.

- `writeSolution()`:

    **Description**\
        Writes to output the solution file.

    **Parameters**\
        `problemName`: (`str`) name of the problem\
        `dimension`: (`int`) the number of cities\
        `algoName`: (`str`)name of the algorithm\
        `executionTime`: (`int`) algorithm execution time\
        `dateTime`: (`str`) time when the algorithm runs\
        `outputFolder`: (`str`) path to the output folder\
        `stepByStep=None`: (`list`) a list contains all Solution objects through the process\
        `comment=''`: (`str`) comment of the process

    **Return**\
        None.

- `__getTotalDistance()`:

    **Description**\
        Private method that calculates the total distance of the current solution.

    **Parameters**\
        None.

    **Return**\
        An `int` number.

- `__getErrorTotalDistance()`:

    **Description**\
        Private method that check if the total distance of the current solution is valid.

    **Parameters**\
        None.

    **Return**\
        Return `None` if the total distance is valid,
        otherwise, return a `list` that contains the valid and the current total distances.

- `__getErrorCustomersNumber`:

    **Description**\
        Private method that check if the number of customers in the current solution is valid.

    **Parameters**\
        None.

    **Return**\
        Return `None` if the number of customer is valid,
        otherwise, return a `list` that contains the valid and the current numbers of customers.

- `__getErrorCustomers`:

    **Description**\
        Private method that check if exists duplicate customer(s).

    **Parameters**\
        None.

    **Return**\
        Return `None` if every customer apppears once,
        otherwise, return a `list` that contains the duplicate customers.

- `__getErrors`:

    **Description**\
        Private method that check the solution's valid conditions.

    **Parameters**\
        None.

    **Return**\
        A `list` of error messages.