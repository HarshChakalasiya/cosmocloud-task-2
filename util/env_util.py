from environs import Env


class EnvUtil:
    def get_env(self, vars: str):
        env = Env()
        env.read_env("config/.env")
        return env(vars)
