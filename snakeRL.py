import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()

#sets font to print the score with
font = pygame.font.SysFont('arial', 25)

#sets constants for the 4 directions
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

#just creates a point object so you can easily access x coordinate, and y coordinate
Point = namedtuple('Point', 'x,y')

#rgb colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE1 = (0, 0, 255)
BLUE2 = (0, 100, 255)
BLACK = (0, 0, 0)

BLOCK_SIZE = 20     #size of the blocks in the "grid"
SPEED = 10        

class SnakeGame:

    def __init__(self, w=640, h=480):
        self.w = w
        self.h = h
        # init display
        self.display = pygame.display.set_mode((self.w, self.h))    #I think this creates the window
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        # init game state
        self.direction = Direction.RIGHT        #start the snake going to the right

        self.head = Point(self.w/2, self.h/2)
        self.snake = [self.head, Point(self.head.x-BLOCK_SIZE, self.head.y), 
                      Point(self.head.x-(2*BLOCK_SIZE), self.head.y)] 
        
        self.score = 0
        self.food = None
        self._place_food()

    #helper function to place food
    #gives random position somewhere in the screen that is a multiple of the BLOCK_SIZE
    def _place_food(self):
        x = random.randint(0, (self.w-BLOCK_SIZE)//BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.h-BLOCK_SIZE)//BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x,y)
        if self.food in self.snake:
            self._place_food()  #recursively call _place_food until the food is not inside of the snake

    
    def play_step(self):
        # 1. collect user input
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN:
                    self.direction = Direction.DOWN

        # 2. move
        self._move(self.direction) #update the head
        self.snake.insert(0, self.head)         #adds another block to the snake (will remove the block at the end of the snake if no food is eaten )

        # 3. check if game over
        game_over = False
        if self._is_collision():
            game_over = True
            return game_over, self.score

        # 4. place new food or just move
        if self.head == self.food:
            self.score += 1
            self._place_food()
        else:
            self.snake.pop()        #removes the last element of the snake

        # 5. update ui and clock
        self._update_ui()
        self.clock.tick(SPEED)

        # 6. return game over and score
        return game_over, self.score
    
    def _is_collision(self):
        # hits boundary
        if self.head.x > self.w - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.h - BLOCK_SIZE or self.head.y < 0:
            return True
        # hits itself
        if self.head in self.snake[1:]:
            return True
        
        return False
    
    def _update_ui(self):
        self.display.fill(BLACK)    #fill screen with black

        for pt in self.snake:
            pygame.draw.rect(self.display, BLUE1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))   #draw the snake
            pygame.draw.rect(self.display, BLUE2, pygame.Rect(pt.x+4, pt.y+4, 12, 12)) 

            pygame.draw.rect(self.display, RED, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))  #draw the food

            text = font.render("Score: " + str(self.score), True, WHITE)
            self.display.blit(text, [0, 0]) #display text in the upper left
            pygame.display.flip()

    def _move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.DOWN:       #y starts at 0 at the top so you add to y to go down
            y += BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE

        self.head = Point(x, y) 

    def step( self , action , create_visual = False ) : 
        """
        Input: The Action. 
            1. 1 is equal to right. 
            2. 2 is equal to left. 
            3. 3 is equal to up. 
            4. 4 is equal to down. 
        Output: The State. 
            1. State Array. 
                1.a. A 1 for each location if there is a snake. 
                1.b. A 0 for each location if there is not a snake. 
                1.c. The row location of the head. 
                1.d. The column location of the head. 
                1.e. The row location of the food. 
                1.f. The column location of the food. 
            2. Reward. 
            3. Done. 
        """ 

        # 1. Collect the user input. 
        if action == 1 : 
            self.direction = Direction.RIGHT  
        if action == 2 : 
            self.direction = Direction.LEFT 
        if action == 3 : 
            self.direction = Direction.UP 
        if action == 4 : 
            self.direction = Direction.DOWN 

        # 2. Move. 
        self._move(self.direction) # Update the head. 
        self.snake.insert(0, self.head) # Add another block to the snake (will remove the block at the end of the snake if no food is eaten ). 

        # 3. Check if game over. 
        game_over = False
        if self._is_collision():
            game_over = True 

        # 4. Put a new food or make a move. 
        if self.head == self.food:
            self.score += 1
            self._place_food()
        else:
            self.snake.pop() # Remove the last element of the snake. 

        # 5. Update the UI and the clock. 
        if create_visual == True : 
            self._update_ui() 
            self.clock.tick(SPEED) # TO DO: I don't know how this work. 

        # 6. Return the State, Reward, and the Done. 

        # The self.h * self.w is the state matrix. 
        # The + 4 is for the row location of the head, and the food and the column location of the head, and the food. 
        # I assume that we are going to use a function approximator. 
        # Therefore, if the range of the value in for the state matrix is 0 or 1, the row, column location of the food and the head need to be [ real_row_location / self.h ] and [ real_column_location / self.w ]. 
        # TO DO: This is not efficient. 
        # TO DO: Implement a new approach, use a matrix. 
        # TO DO: The above approach is not too good. 
        # TO DO: We need to increase the size of the list. 

        state_list = [ 0 for _ in range( ( self.h * self.w ) + 4 ) ] 
        state_list[ self.h * self.w ] = int( self.food.x ) / self.w 
        state_list[ self.h * self.w + 1 ] = int( self.food.y ) / self.h 
        state_list[ self.h * self.w + 2 ] = int( self.head.x ) / self.w 
        state_list[ self.h * self.w + 3 ] = int( self.head.y ) / self.h 
        for the_matrix_loc in self.snake : 
            index = int( the_matrix_loc.x ) * self.h + int( the_matrix_loc.y ) 
            state_list[ index ] = 1 

        # TO DO: Get the desicion from the group, do we give the +1 reward each time, or do we given the total reward once the game is over. 
        reward = 0 
        if game_over == True : 
            reward = self.score 

        # Return. 
        return state_list , reward , game_over 

    def reset( self ) : 
        """
        Go back to the start of the game. 
        """
        pass 

    def render( self ) : 
        """
        Create a visual for the current state. 
        """
        pass 

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
            self.learn() 
            if iteration % test_interval == 0 : 
                result = self.evaluate( trial_count ) 
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

    def get_greedy_action( self ) : 
        """ 
        1. Get the greedy action. 
        """
        pass 

    def get_explore_exploit_action( self ) : 
        """
        1. Get the action according to the explore exploit. 
        2. Update the state in order to decrease the random action at each step. 
        """ 
        pass 

########################## 
# 
# How To Run It: 
# agent = Agent() 
# result = agent.learn_and_then_evaluate() 
# 
# At this time, the result is how good that the agent did. 
# We can test it, using just the evaluate. 
# 
##########################

if __name__=='__main__': 

    test = True 

    if test == True : 
        for _ in range( 100 ) : 
            snake = SnakeGame() 
            done = False 
            while done == False : 
                random_integer = random.randint(1, 4) 
                print( random_integer ) 
                """random_integer = 4 
                print( random_integer ) """
                state_list , reward , done = snake.step( random_integer , True ) 
                snake_loc = [ index for index, value in enumerate(state_list ) if value == 1 ] 
                print( snake_loc , random_integer , reward , done ) 

    else : 

        # Play the game manually. 
        game = SnakeGame() 
        while True:
            game_over, score = game.play_step()
            if game_over == True:
                break 
        print('Final Score', score)
        pygame.quit() 

