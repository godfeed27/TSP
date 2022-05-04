# Solution file structure

- `NAME`: Problem name.
- `COMMENT`: 
- `DIMENSION`: Number of customers.
- `DISTANCE`: Total distance of the tour.
- `EXECUTION_TIME`: Time run of the algorithm (second), excluding the time for reading or calculating the distance matrix.
- `TOUR_SECTION`: The next line contains the solution tour where the customers are separated by spaces.
- `STEP_BY_STEP_TOURS`: The next lines contain the tours attained while running the algorithm.

Example:
```
NAME : ulysses22
COMMENT :
DIMENSION : 22
DISTANCE : 7013
EXECUTION_TIME : 100.00s
TOUR_SECTION
1 8 18 4 22 17 2 3 16 21 20 19 10 9 11 5 15 6 7 12 13 14

STEP_BY_STEP_TOURS
1 8 18 4 22 17 2 3 16 21 20 19 10 9 11 5 15 6 7 12 13 14
EOF
```