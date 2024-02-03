# Water_Pitcher_Problem
 
Problem Statement: 
Implement a program that reads this input file and calculates the shortest path (number of
steps) from initial state (all pitchers are empty) to the final state (where the “infinite”
The capacity pitcher has the target quantity. Implement an informed search (A*) for this problem. 

Theoretical Implementation:

The Python program I implemented uses A* search algorithm to solve the water jug problem. The theoretical implementation involves the following steps:

Heuristic Calculation: The heuristic function calculate_heuristic calculates the estimated cost to reach the goal from the current state. It’s defined as the difference between the goal and the current state if the current state is less than or equal to the goal, otherwise it returns infinity.

A Search*: The A_star_search function implements the A* search algorithm. It starts with an initial state where all jugs are empty and uses a priority queue to store states to be visited, ordered by their heuristic value. It then iteratively pops the state with the lowest heuristic value from the queue, checks if the goal has been reached, and if not, generates all possible next states by pouring water between pitchers. These next states are then added to the queue to be visited.

Lower Bound: 
The lower bound of an A* search algorithm depends on the heuristic used. In this case, the heuristic function is defined by the calculate_heuristic function, which estimates the remaining distance from the current state to the goal state. The A* algorithm guarantees optimality (finding the shortest path) when the heuristic is admissible. Therefore, in this case, the lower bound for the A* algorithm is the true cost of the optimal solution, which is the minimum number of steps needed to reach the target_goal from the initial state
