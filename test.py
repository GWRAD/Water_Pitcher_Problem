import unittest
import sys
from Water_pitcher_prblm import calculate_heuristic, A_star_search

class TestAStar(unittest.TestCase):
    
    # Test if the heuristic function is admissible, i.e. never overestimates the actual cost
    def test1_calculate_heuristic_admissible(self):
        current_state = [2,5,6,72] # The current capacities of the water pitchers
        target_quantity = 143 # The target quantity of water to be measured
        h = calculate_heuristic(current_state, target_quantity) # The heuristic value
        self.assertTrue(h >= 0) # The heuristic value should be non-negative

    # Test another case of the heuristic function being admissible
    def test2_calculate_heuristic_admissible(self):
        current_state = [3,6]
        target_quantity = 2
        h = calculate_heuristic(current_state, target_quantity)
        self.assertTrue(h >= 0)

    # Test a case where the heuristic function is zero, i.e. the current state is the goal state
    def test3_calculate_heuristic_admissible(self):
        current_state = [2]
        target_quantity = 2
        h = calculate_heuristic(current_state, target_quantity)
        self.assertTrue(h == 0)

    # Test a case where the heuristic function is positive, i.e. the current state is not the goal state
    def test4_calculate_heuristic_admissible(self):
        current_state = [2,3,5,19,121,852]
        target_quantity = 11443
        h = calculate_heuristic(current_state, target_quantity)
        self.assertTrue(h > 0)

    # Test if the A* search algorithm returns the optimal number of steps to reach the target quantity
    def test1_A_star_search(self):
        capacities = [2,5,6,72] # The maximum capacities of the water pitchers
        target_quantity = 143 # The target quantity of water to be measured
        s = A_star_search(capacities,target_quantity) # The number of steps returned by the algorithm
        self.assertTrue(s==26) # The optimal number of steps is 26

    # Test a case where the A* search algorithm returns -1, indicating that the target quantity is impossible to measure
    def test2_A_star_search(self):
        capacities = [3,6]
        target_quantity = 2
        s = A_star_search(capacities,target_quantity)
        self.assertTrue(s==-1)

    # Test another case where the A* search algorithm returns -1, indicating that the target quantity is impossible to measure
    def test3_A_star_search(self):
        capacities = [2]
        target_quantity = 143
        s = A_star_search(capacities,target_quantity)
        self.assertTrue(s==-1)

    # Test a case where the A* search algorithm returns a large number of steps, indicating that the target quantity is difficult to measure
    def test4_A_star_search(self):
        capacities = [2,3,5,19,121,852]
        target_quantity = 11443
        s = A_star_search(capacities,target_quantity)
        self.assertTrue(s==36) # The optimal number of steps is 36


if __name__ == '__main__':
    unittest.main()
