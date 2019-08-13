"""
This script implement an ant agent that randomly executes a set of
pre-trained skills in a four rooms environment.  The skills are constructed
using a trained 3-level HAC agent. The three pre-trained skills used in this
script include options that
    (1) move agent to northern door of room,
    (2) move agent to center of room,
    (3) move agent to southern door of room.

To modify the set of skills, update the  "execute_skill.py" and
"agent.py" files.

To run this script, enter the command "python3 run_random_agent.py --show --subgoals".
Removing the "--subgoals" option will hide the HAC subgoals.  Removing the
"--show" option will not visualize training.
"""

from design_agent_and_env import design_agent_and_env
from options import parse_options
from agent import Agent
from run_HAC import run_HAC
from execute_skill import execute_skill
import numpy as np

"""
Determine settings specified by user.  Relevant settings include
    (1) --subgoals (Show HAC subgoals)
    (2) --show (Visualize agent in environment)
    (3) --verbose (Print every transition that occurs at every level)
"""
FLAGS = parse_options()

# Load pre-trained agent and ant four rooms environment.
agent, env = design_agent_and_env(FLAGS)

# Run agent that executes random skills.
for episode in range(50):

    # Determine initial state for agent.  Below function will randomly place agent in one of four rooms.
    state = env.reset_sim()

    for attempt in range(25):

        """
        Determine skill to execute.  Code currently enables agent to execute one of 3 skills.
            - Skill "0" attempts to move agent to northern door of current room.
            - Skill "1" moves agent to center of current room.
            - Skill "2" moves agent to southern door of current room.
        """
        action = np.random.randint(3)

        # Execute option and return next state
        state = execute_skill(agent, env, state, action)
