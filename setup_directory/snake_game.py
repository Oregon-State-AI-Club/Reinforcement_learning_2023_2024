import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()
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
REWARD_DESIGN = 1 # 1: +1 each time the score increase, 2: The +self.score when the game is done. 

class SnakeGame:

    def __init__(self, create_visual=True, w=640, h=480):
        self.w = w
        self.h = h
        # init display
        if (create_visual):
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
        self.reward_to_give = 0     

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
            self.reward_to_give += 1 
            self.score += 1 
            self._place_food()
        else:
            self.snake.pop() # Remove the last element of the snake. 

        # 5. Update the UI and the clock. 
        if create_visual == True : 
            self.render() 

        # 6. Return the State, Reward, and the Done. 
        if REWARD_DESIGN == 1 : 
            reward = self.reward_to_give 
            self.reward_to_give = 0 
        if REWARD_DESIGN == 2 : 
            reward = 0 
            if game_over == True : 
                reward = self.score 
        state = self.get_the_state_representation() 
        return state , reward , game_over 

    def reset( self ) : 
        """
        Go back to the start of the game. 
        """
        pass 

    def render( self ) : 
        """
        Create a visual for the current state. 
        """ 
        self._update_ui() 
        self.clock.tick( SPEED ) 

    def get_the_state_representation( self ) : 
        """
        Return the state in Raw form, that the game represent. 
        """
        return ( self.snake , self.direction , self.head , self.score , self.food , self.h , self.w , BLOCK_SIZE ) 
