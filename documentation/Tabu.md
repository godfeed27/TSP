# Tabu

**Tabu Search** is an algorithm that inherits from the Hill Climbing algorithm. Also, overcome the weakness of being trapped in the local optimal region by allowing the solution to traverse the inefficient regions and avoid falling into a cycling with tabus

## <a name="parameters"></a>Parameters
Tabu Search version in `Tabu.py` requires some parameters below:
- `dataModel`: a `dataModel` instance (introduced in [DataModel.md](https://github.com/optimahus/TSP/blob/main/documentation/DataModel.md))
- `neighborSize`: the number of neighbors to search to improve mobility, calculated as neighborSize times the number of customers
- `tabusSize`: the size of the tabus, calculated as tabusSize times the number of customers
- `timeLimit`: time limit for the whole algorithm to solve
- `verbose`: a number that decides how much detailed the output should be.

## Code structure
In `Tabu.py`, class `Tabu` has the following methods:

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
    - `dataModel`: A `dataModel` instance
    - `constantDict`: A parameter dictionary
    - `timeLimit`: Time limit for the whole algorithm to solve

    **Return**\
        An instance of the class.

- `__initialSolution()`:

    **Description**\
        Private method that generates a starting `Greedy` solution .

    **Parameters**\
        None.

    **Return**\
        An instance of class `Solution`.
        
- `__createNeighborList()`:

    **Description**\
        Private method that create a neighbors set of moves

    **Parameters**\
        `quantityCustomer`: Customers number.

    **Return**\
        A list set of moves neighbors.

- `__updateBestSolution()`:

    **Description**\
        Private method that update current solution become best solution.

    **Parameters**\
        `solution`: A solution.

    **Return**\
        None.

- `__distanceVariesTwoOpt()`:

    **Description**\
        Private method that calculate the change when swapping two edges.

    **Parameters**\
        `solution`: A solution.
        `neighbor`: List of two changing edges.

    **Return**\
        Total change.

- `__swap2Edges()`:

    **Description**\
        Private method that perform a two-edge swap and distance varies change in the solution.

    **Parameters**\
        `indexNeighborChange`: index of location changes.
        `solution`: a solution.
        `distanceVariesChange`: total distance if make change.

    **Return**\
        None.
        
- `__checkTabus()`:

    **Description**\
        Private method that check the change is tabu or not by customer index is in tabus or not.

    **Parameters**\
        `indexNeighborChange`: index of location changes.
        `tabus`: list of recent changes.

    **Return**\
        Boolean.        
        
- `__updateTabus()`:

    **Description**\
        Private method that update Tabus by add customer index changed in current solution.

    **Parameters**\        
        `tabus`: List of recent changes.
        `indexNeighborChange`: Index of location changes.
        `quantityCustomer`: Customers number.

    **Return**\
        None.        

- `__updateMatrix()`:

    **Description**\
        Private method that update matrix every time two customers swap places.

    **Parameters**\        
        `diversificationMatrix`: Matrix that stores the number of exchanges between customers.
        `indexNeighborChange`: Index of location changes.
        `solution`: A solution.

    **Return**\
        None. 
        
- `__compareToCurrentSol()`:

    **Description**\
        Private method that check a move is improve or not.

    **Parameters**\        
        `distanceVariesChange`: Total distance if make change.

    **Return**\
        Boolean.    
        
- `__compareToBestSol()`:

    **Description**\
        Private method that check current solution is better than best solution or not.

    **Parameters**\        
        `solution`: A solution.

    **Return**\
        Boolean.    
        
- `__localSearch()`:

    **Description**\
        Private method that improve the solution within a certain period of time

    **Parameters**\        
        `tabus`: List of recent changes.
        `quantityCustomer`: Customers number.
        `timeLimit`: A predetermined period of time.

    **Return**\
        Time remaining.    
        
- `__improveSolutions()`:

    **Description**\
         Private method that improve list of solution within a certain period of time.

    **Parameters**\        
        `solutionList`: List of solution.
        `quantityCustomer`: Customers number.
        `allocateTime`: A predetermined period of time.

    **Return**\
        None.       

- `__compareTwoSolution()`:

    **Description**\
         Private method that cmpare two solutions to see if they are the same.

    **Parameters**\        
        `solution1`: A solution.
        `solution2`: A solution.

    **Return**\
        Boolean.       
        
- `__allocateTimeForSections()`:

    **Description**\
         Private method that allocate time for solution-finding and solution-improvement sections.

    **Parameters**\        
        `quantityCustomer`: Customers number.

    **Return**\
        Time allocation ratio.        
        
- `__mainTabu()`:

    **Description**\
         Private method that to find better solution.

    **Parameters**\        
        `currentSolution`: Current solution
        `quantityCustomer`: Customers number.
        `tabus`: List of recent changes.
        `diversificationMatrix`: Matrix that stores the number of exchanges between customers.
        `terminationCriteriaStatus`: Confirmation condition has made a improve move.

    **Return**\
        `terminationCriteriaStatus` 
        
- `solve()`:

    **Description**\
        Solves the problem by running multiple loops of annealing and prints the process based on the `verbose` parameter.

    **Parameters**\
        None.

    **Return**\
        An instance of class `Solution`.        