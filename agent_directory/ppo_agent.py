from ..setup_directory.agent import Agent 
import numpy as np
import matplotlib.pyplot as plt 

class DqnAgent( Agent ) : 
    
    def __init__( self ) : 
        super().__init__()  

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

    def _change_the_state_representation( self , state )  : 
        """ 
        Turn the raw state representation, to a useful state representation. 
        """ 
        pass 