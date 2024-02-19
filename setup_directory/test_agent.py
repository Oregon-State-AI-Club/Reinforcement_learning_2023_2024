from .agent import Agent 
from .snake_game import SnakeGame 
import random 
import numpy as np
import matplotlib.pyplot as plt 

class TestAgent( Agent ) : 
    """
    1. This is just an Agent, in order to make sure that the Agent-Environment interface is correct. 
    """

    def __init__( self ) : 
        super().__init__() 

    def _get_random_action( self , direction ) : 
        """
        1. Return a random action. 
        2. It the previous action is 1 and the current action is 2, this is a guaranteed death. 
        3. Try to avoid this, as the current function is just to test that the interface is currently working. 
        """ 
        how_to_die = { 1 : 2 , 2 : 1 , 3 : 4 , 4 : 3 } 
        random_integer = random.randint(1, 4) 
        while random_integer == how_to_die[ direction ] : 
            random_integer = random.randint(1, 4) 
        return random_integer 

    def evaluate_random_policy( self , trial_count , create_visual = False ) : 
        """ 
        1. Evaluate a random model. 
        2. Return the reward for each trial. 
        """
        return_list = [] 
        for i in range( trial_count ) : 
            self.simulator = SnakeGame() 
            action = 1 
            done = False 
            total_reward = 0 
            while done == False : 
                action = self._get_random_action( action ) 
                state , reward , done = self.simulator.step( action , create_visual ) 
                total_reward += reward 
            return_list.append( total_reward ) 
        return return_list 

