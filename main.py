from setup_directory.snake_game import SnakeGame 
from setup_directory.test_agent import TestAgent 
import pygame 
import sys 

if __name__=='__main__': 

    test = sys.argv[ 1 ] 
    show_visual = True
    if test == "test_semi_random_policy" : 
        show_visual = bool(int(sys.argv[ 2 ])) # 1 or 0
        agent = TestAgent() 
        result = agent.evaluate_random_policy( 10 , show_visual )
        for iteration in range( len( result ) ) : 
            print( f"The total reward from the iteration { iteration + 1 }: { result[ iteration ] }. ") 

    if test == "play_the_game_manually" : 
        # Play the game manually. 
        game = SnakeGame(show_visual)
        while True:
            game_over, score = game.play_step()
            if game_over == True:
                break 
        print('Final Score', score)
        pygame.quit() 
