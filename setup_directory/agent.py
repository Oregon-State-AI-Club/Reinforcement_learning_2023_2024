from .snake_game import SnakeGame 
import numpy as np
import matplotlib.pyplot as plt 
import random 

class Agent: 
    
    def __init__( self ) : 
        """
        1. Initialize the agent. 
        2. Initialize the simulator. 
        """ 
        self.simulator = SnakeGame() 

    def learn_and_then_evaluate( self , train_count , test_interval , trial_count , create_visual_at_train = False , create_visual_at_test = False ) : 
        """ 
        1. Initialize a return list. 
        2. Call learn up to train_count time. 
        3. Each test_interval count call evaluate. 
            2.a. Store the result from the evaluate to the return list. 
        4. Return the return list. 
        """ 

        return_list = [] 
        for iteration in range( train_count ) : 
            self._learn( create_visual_at_train ) 
            if iteration % test_interval == 0 : 
                result = self._evaluate( trial_count , create_visual_at_test ) 
                return_list.append( result ) 
        return return_list 
    
    def _learn( self , create_visual = False ) : 
        """ 
        1. Implement the RL algorithm. 
        """ 
        pass 

    def _evaluate( self , trial_count , create_visual = False ) : 
        """ 
        1. Test the current model up to trial_count time. 
        2. Return the average result. 
        """ 
        pass 

    