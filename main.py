from setup_directory.snake_game import SnakeGame 
from setup_directory.test_agent import TestAgent 
import pygame 
import sys 

if __name__=='__main__': 

    test = sys.argv[ 1 ] 
    
    if test == "test_semi_random_policy" : 
        agent = TestAgent() 
        result = agent.evaluate_random_policy( 10 , True ) 
        for iteration in range( len( result ) ) : 
            print( f"The total reward from the iteration { iteration + 1 }: { result[ iteration ] }. ") 

    if test == "play_the_game_manually" : 
        # Play the game manually. 
        game = SnakeGame() 
        while True:
            game_over, score = game.play_step()
            if game_over == True:
                break 
        print('Final Score', score)
        pygame.quit() 
