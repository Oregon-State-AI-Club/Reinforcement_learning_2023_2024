from snake_game import SnakeGame 
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
            self.learn( create_visual_at_train ) 
            if iteration % test_interval == 0 : 
                result = self.evaluate( trial_count , create_visual_at_test ) 
                return_list.append( result ) 
        return return_list 

    def learn( self , create_visual = False ) : 
        """ 
        1. Implement the RL algorithm. 
        """ 
        pass 

    def evaluate( self , trial_count , create_visual = False ) : 
        """ 
        1. Test the current model up to trial_count time. 
        2. Return the average result. 
        """ 
        pass 

    ################################## 

    def get_random_action( self , direction ) : 
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
                action = self.get_random_action( action ) 
                raw_state , reward , done = self.simulator.step( action , create_visual ) 
                real_state = self.change_the_state_representation( raw_state ) 
                total_reward += reward 
            return_list.append( total_reward ) 
        return return_list 

    def change_the_state_representation( self , state ) : 
        """ 
        Turn the raw state representation, to a useful state representation. 
        """ 

        # Initialize the state Matrix. 
        height = state[ 5 ] / state[ 7 ] 
        width = state[ 6 ] / state[ 7 ]
        state_matrix = np.zeros( ( int( height ) , int( width ) ) ) 

        # If there is a snake, it is 1. 
        for point in state[ 0 ] : 
            # Here, implement this by checking if there is a collision, I was lazy here. 
            try : 
                state_matrix[ int( point.y / state[ 7 ] ) ][ int( point.x / state[ 7 ] ) ] = 1 
            except : 
                print( "Collision. ") 

        # Uncomment this if you want to check if the state matrix is correct. 
        # self.test_if_state_matrix_is_correct( state_matrix ) 

        # Initialize the rest of the state. 
        food_x = state[ 4 ].x 
        food_y = state[ 4 ].y 
        head_x = state[ 2 ].x 
        head_y = state[ 2 ].y  
        the_direction = state[ 1 ] 
        the_score = state[ 3 ] 

        # Return the new state representation. 
        return ( state_matrix , food_x , food_y , head_x , head_y , the_direction , the_score ) 

    def test_if_state_matrix_is_correct( self , the_matrix ) : 
        plt.imshow( the_matrix , cmap='viridis' , interpolation='none' ) 
        plt.colorbar() 
        plt.show() 

    ################################## 

        