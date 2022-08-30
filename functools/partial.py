from functools import partial
from icecream import ic


def load_training_info(agent_id, agent_name, agent_env, agent_action_space, agent_obs):
    """

    :param agent_id:
    :param agent_name:
    :param agent_env:
    :param agent_action_space:
    :param agent_obs:
    :return:
    """
    return agent_id, agent_name, agent_env, agent_action_space, agent_obs


agent_1_config = {
        "agent_id": 'agent_01',
        "agent_name": "jack",
        "agent_env": 'foot_ball',
        "agent_action_space": list(range(6))
    }

load_agent_1_obs = partial(load_training_info, **agent_1_config)

print(load_agent_1_obs)
ic(load_agent_1_obs(agent_obs=[0.1, 0.2, 0.3, 0.4], agent_env='dota2'))