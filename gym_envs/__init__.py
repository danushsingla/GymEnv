from gym.envs.registration import register

register(
    id="gym_envs/GridWorld-v0",
    entry_point="gym_envs.envs:GridWorldEnv",
)

register(
        id='gym_envs/PongGame',
        entry_point='gym_envs.envs:PongEnv',
    )