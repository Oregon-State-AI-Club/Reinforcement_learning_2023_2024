# Reinforcement Learning 2023 - 2024. 

- The creation of a reinforcement learning agent that interact with a traditional Snake Game. 

### Agent Directory. 

1. In this directory, for every RL Algorithm we are going to implement, we can create a new Agent that inherit from the main Agent class, in the setup directory, then change the method's learn, evaluate and thechange_the_state_representation. 
2. There are 2 files, right now, dqn_agent, where we can implement an Agent that use a Deep Q Network, and a ppo_agent, where we can implement an Agent that use Proximal Policy Optimization. 
3. If you have an algorithm or idea you have, you are welcome to create a new file and implement your agent there. 

### Setup Directory. 

1. In this directory, there are 3 files, agent.py, which is the parent class for all of the RL agent's, snake_game.py which is the code for the environment and the game, and there is test_agent.py, which is an Agent just to test and make sure the Agent-Simulator interface is working correctly, and the project is setup well. 
2. You don't need to modify anything in this directory. 

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

## Important. 

1. Currently, we have a snake game, where you can interact and play with it manually, or you can train an agent with a similar way that you can train an agent in an environment such as one of the OpenAI Gym environment. 

2. Once you have created the environment, you can use the step( action ) function, to interact with the environment. The step( action ) function return 3 thing, state, reward, and the done which is True if the game is over and False if it is not. The state, you are going to recieve here is the game's internal state representation, you need to implement/call the method change_the_state_representation in your agent to change this state representation into something that is useful. 

## How to run it. 

1. If you want to just play the game manually, in the terminal enter "python3 main.py play_the_game_manually". 
2. If you want to test the semi random policy which is used to make sure the model-simulator interface work correctly, in the terminal enter "python3 main.py test_semi_random_policy". 

