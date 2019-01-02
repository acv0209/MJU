import gym
from gym.envs.registration import register
import sys
import msvcrt

# MACROS
LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

# Key mapping
arrow_keys = {
    72: UP,
    80: DOWN,
    77: RIGHT,
    75: LEFT}

# Register FrozenLake with is_slippery False
register(
    id='FrozenLake-v3',
    entry_point='gym.envs.toy_text:FrozenLakeEnv',
    kwargs={'map_name': '4x4', 'is_slippery': False}
)

env = gym.make('FrozenLake-v3')
env.render()  # Show the initial board

while True:
    # Choose an action from keyboard
    
    if msvcrt.kbhit():
        key1 = ord(msvcrt.getch())  #  inkey()
        key = ord(msvcrt.getch())  #  inkey()
        print(key1)
        print(key)
        if key not in arrow_keys.keys():
            print("Game aborted!")
            break

        action = arrow_keys[key]
        state, reward, done, info = env.step(action)
        env.render()  # Show the board after action
        print("State: ", state, "Action: ", action,
              "Reward: ", reward, "Info: ", info)

        if done:
            print("Finished with reward", reward)
            break
