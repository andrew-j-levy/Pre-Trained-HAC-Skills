This repository provides software to construct skills using pre-trained Hierarchical Actor-Critic (HAC) agents.  

As an example, executing the command *python3 run_random_agent.py --show --subgoals* will implement an ant agent in a four rooms enivronment that randomly executes a set of three skills, which include 

1. Move to northern door of room
2. Move to center of room
3. Move to southern door of room.

To visualize the skills without the HAC subgoals, remove the *--subgoals* option.  To train agent without the visualization, remove the *--show* option.

Skills can be constructed using the *execute_skill.py, agent.py,* and *environment.py* files.
