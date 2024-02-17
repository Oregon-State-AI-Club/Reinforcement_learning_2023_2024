# Reinforcement Learning 2023 - 2024. 

- The creation of a reinforcement learning agent through the medium of a snake game. 

## How to use this Template. 

### Snake Game. 

1. The Snake Game is a game made with PyGame, it is modified, to also function as a simulator, to train the Reinforcement Learning Agent. 
2. You can play the game manually if you want, using the command "python3 main.py play_the_game_manually". 
3. It also has method's, that allow the Agent to interact with it. 
4. The important method here is the Step method. This method input an action, which is an integer from 0 to 3, associated with a direction, and return state, reward, done. The state here is the game's internal state representation. This is modified in the agent, and there is a method for that. 
5. You don't need to understand how this work, in depth, in order to use it, however, understand the Step method and how it work. 

### Agent. 

1. The Agent is where you train the Reinforcement Learning Algorithm. 
2. There is a method called learn_and_evaluate, which call the learn method, where you need to implement the algorithm, it then call the evaluate method. 
3. In the learn method, to interact with the environment, you need to call the Step method of the environment, which then return a raw state. 
4. Then, you can call you own method, in order to convert this raw state representation in to a state representation you want. 
5. There is already a default, method for this, called change_the_state_representation, it is fine, however we will need to change it, I think. 
6. There is already a code, to test a semi-random policy, which can act as an inspiration to write a better evaluate method. 
7. Feel free to create a class that inherit from this agent, and then you can implement your own learn, evaluate, and change_the_state_representation method. 

## The Documentation. 

- Currently, we have a snake game, where you can interact and play with it manually, or you can train an agent with a similar way that you can train an agent in an environment such as one of the OpenAI Gym environment. 

- Once you have created the environment, you can use the step( action ) function, to interact with the environment. The step( action ) function return 3 thing, state, reward, and the done which is True if the game is over and False if it is not. 

## How to run it. 

1. If you want to just play the game manually, in the terminal enter "python main.py play_the_game_manually". 

2. If you want to test the semi random policy which is used to make sure the model-simulator interface work correctly, in the terminal enter "python main.py test_semi_random_policy". This is going to test the semi random policy, and then it is going to print the total reward for each test. 

3. The game represent's the state in a way that is difficult to use function approximation, there is a method at the Agent that turn this raw state in to a numpy matrix of the game board, with 0 if there is not a snake, and 1 if there is a snake. The return state from this method is  ( state_matrix , food_x , food_y , head_x , head_y , the_direction , the_score ). From here we can decide on the best way to represent it, this is a start, though. 

## The Resources. 

1. https://www.youtube.com/watch?v=suEjzb8Qmls&list=PLwQpgP0y-0JhEgfy39QfHzxGmdq9ilM8J. This is a lecture series from the past. I think that this is from a Reinforcement Learning class from a professor at OSU at 2019. It is a good resource. 

2. https://www.youtube.com/watch?v=jds0Wh9jTvE&list=PL_iWQOsE6TfVYGEGiAOMaOzzv41Jfm_Ps&index=9. This is also very well known, it is long, however I think that Lecture 4 might be quite relevant. 
