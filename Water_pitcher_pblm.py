import sys
import heapq

INFINITY = float('inf')

def calculate_heuristic(state: list, goal:int) -> int:
    """Calculate the heuristic value for a given state and goal.
    """
    if state[-1] <= goal:
        return goal - state[-1]
    else:
        return  INFINITY

#A* Algortihm
def A_star_search(pitcher_capacities: list, target_goal: int) -> int:
    """Find the minimum number of transfers to measure the target amount of water using the A* search algorithm.
    """
    #Base case: Check if the input values are valid.
    if target_goal < 0 or min(pitcher_capacities) <=0:             
        return -1
    #Add an infinite capacity pitcher to the list.
    pitcher_capacities = pitcher_capacities + [INFINITY]            
    #Initialize the state with all jugs empty.
    initial_state = [0]* len(pitcher_capacities)
    #Initialize a priority queue with (heuristic, step, transfer, state).
    priority_queue = [(calculate_heuristic(initial_state, target_goal), 0, 0, initial_state)]   
    
    visited_states = set()

    
    while priority_queue:
        #Pop the node with the lowest f-value from the priority queue.
        heuristic_value, current_step, current_transfer, current_state = heapq.heappop(priority_queue)
        #print(priority_queue)
        #Check if the goal is reached.
        if current_state[-1] == target_goal:
            return current_transfer
        #Check if the goal is exceeded.
        elif current_state[-1] > target_goal:
            continue

        #Check if the current state is already visited.
        if tuple(current_state) not in visited_states :
            visited_states.add(tuple(current_state))
            
            

            #Explore next states by pouring water between pitchers.
            for i in range(len(pitcher_capacities)):
                for j in range(len(pitcher_capacities)):
                    #Skip the case where i and j are the same.
                    if i ==j:
                        continue                    

                    
                    next_state = current_state.copy()
            

                    #Pour water from pitcher i to pitcher j.
                    if next_state[j] == 0 and i != len(pitcher_capacities) - 1:
                        #Fill pitcher j with the capacity of pitcher i.
                        next_state[i] = pitcher_capacities[i]
                    else:
                        if j != len(pitcher_capacities) - 1:
                            #Check if pitcher i has enough water to fill pitcher j.
                            if (next_state[i] + next_state[j] <= pitcher_capacities[i]):
                                #Pour all the water from pitcher i to pitcher j.
                                next_state[i] += next_state[j]
                                next_state[j] = 0
                            else:
                                #Pour as much water as possible from pitcher i to pitcher j.
                                difference = pitcher_capacities[i] - next_state[i]
                                next_state[i] = pitcher_capacities[i]
                                next_state[j] -= difference
                        else:
                            #Fill pitcher i with its capacity.
                            next_state[i] = pitcher_capacities[i]
                    #Check if the next state is already visited.
                    if tuple(next_state) not in visited_states:
                        #Calculate the f-value for the next state.
                        f_value = current_step + 1 + calculate_heuristic(next_state, target_goal)
                        #Increment the transfer count by one.
                        next_transfer = current_transfer + 1 
                        
                        #Push the next node to the priority queue.
                        heapq.heappush(priority_queue, (f_value, current_step + 1, next_transfer, next_state))
                        
    
        #print("Visited States: "+ format(visited_states))
        #print(priority_queue)
    #Return -1 if the goal is unreachable.
    return -1


# Function to read input from input files
def read_inputs_from_file(filepath):
    """Read the input values from a file.
    """
    with open(filepath, "r") as file:
        #Read the first line and split it by commas.
        capacities = list(map(int, file.readline().split(",")))
        #Read the second line and convert it to an integer.
        goal = int(file.readline())
    #Return the capacities and the goal.
    return capacities, goal

# Main function
if __name__ == '__main__' :
    #Check if the input file is provided as an argument.
    if len(sys.argv) == 2:
        #Read the input values from the file.
        capacities, target_goal = read_inputs_from_file(sys.argv[1])
        #Print the pitcher capacities and the target goal.
        print("Pitcher Capacities: {}" .format(capacities))
        print("Target Goal: {}" .format(target_goal))
        transfers_to_achieve_goal = A_star_search(capacities, target_goal)
        print("Transfers to reach till goal: {}" .format(transfers_to_achieve_goal))
