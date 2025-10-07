
try:
    from stable_baselines3 import PPO
    from stable_baselines3.common.env_util import make_vec_env
except:
    PPO = None
    make_vec_env = None

class RLAgent:
    def __init__(self, env_id='CartPole-v1'):
        self.env_id = env_id
        self.model = None
        try:
            if PPO:
                self.env = make_vec_env(env_id, n_envs=1)
        except Exception as e:
            print(f"RL init falhou: {e}")
