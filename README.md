# Reinforcement Learning 2023 - 2024. 

- The creation of a reinforcement learning agent through the medium of a snake game. 

## The Documentation. 

- Currently, we have a snake game, where you can interact and play with it manually, or you can train an agent with a similar way that you can train an agent in an environment such as one of the OpenAI Gym environment. 
- Once you have created the environment, you can use the step( action ) function, to interact with the environment. The step( action ) function return 3 thing, state, which is a python list ( We can turn this into a NumPy array later. ), reward ( We can figure out the reward design later. ), and the done which is True if the game is over and False if it is not. 
- There is a render() function, where you can actually use pygame to render it. 

## How to run it. 

1. If you want to just play the game manually, in the terminal enter "python snakeRL.py play_the_game_manually". 

2. If you want to test the semi random policy which is used to make sure the model-simulator interface work correctly, in the terminal enter "python snakeRL.py test_semi_random_policy". This is going to test the semi random policy 10 time, and while it is doing the test, it is going to visualize it. When the test is over, it is going to print the total reward for each test. 

## The Roadmap. 

1. Currently, the simulator code interface with the game code, at each step we turn the game's perception of the state to a python list, which can take a lot of time. In the future, we can use a matrix, and then manipulte the matrix according to the given action. 

2. The current state list is a python list, and it for the game matrix, if there is a part of the snake in there it has a 1, if not it has a 0, the rest of the list has the row location of the food and the head, and the column location of the food and the head. The last 4 value is between 1 and 0. I am not sure, in term of the ML perspective if this is ideal. 

3. I don't know which algorithm we are going to use, however we can train them in parallel using the ray library. This is going to be done at the end though, not a current concern. 

## The Resources. 

1. https://arxiv.org/pdf/1312.5602.pdf. I think that this is a well known paper, though they use convolutional network and input the visual information. I am not sure if we can implement it in this term. The other way to do it is to get the state information from the simulator which is more like the way OpenAI Gym environment work. 

2. https://www.youtube.com/watch?v=suEjzb8Qmls&list=PLwQpgP0y-0JhEgfy39QfHzxGmdq9ilM8J. This is a lecture series from the past. I think that this is from a Reinforcement Learning class from a professor at OSU at 2019. It is a good resource. 

3. https://www.youtube.com/watch?v=jds0Wh9jTvE&list=PL_iWQOsE6TfVYGEGiAOMaOzzv41Jfm_Ps&index=9. This is also very well known, it is long, however I think that Lecture 4 might be quite relevant. 

## The Idea. 

1. The Environment: Deterministic-Stochastic. 
2. Is the model known: Yes. 
3. Is the MDP Huge: No-Yes. 

### Value Iteration. [ Dynamic Programming. ]. 

1. Do a Bellman Backup at each state until the error is less than epsilon. 

### Model Based Reinforcement Learning. 

1. Do a Bellman Backup

### Model Free Reinforcement Learning. 

# This is not correct. 
