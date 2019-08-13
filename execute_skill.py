"""
execute_skill function implements the skill transition function.  The function will
take as input the agent object, environment object, current state and selected skill.
The function then executes that skill and returns the next state.
"""

def execute_skill(agent, env, state, action):

    """
    Execute skill by calling the "train" method in the agent class.  This will
    set a new goal state for the pre-trained 3-level HAC agent to achieve.  The new goal
    state will depend on the current state and skill number provided.
    """
    agent.train(env, state, action)

    # Return next state.  State is a concatenation of joint positions and joint velocities.
    return env.get_state()
