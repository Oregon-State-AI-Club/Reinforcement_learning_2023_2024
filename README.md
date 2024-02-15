# Reinforcement Learning 2023 - 2024. 

- The creation of a reinforcement learning agent through the medium of a snake game. 

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
