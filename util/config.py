from util.env_util import EnvUtil


class Params:
    db_host: str
    db_port: str
    db_user: str
    db_password: str
    db_name: str

    max_msg_count: str = None

    def __init__(self):
        self.db_host = EnvUtil().get_env("NOSQL_DB_HOST")
        self.db_port = EnvUtil().get_env("NOSQL_DB_PORT")
        self.db_user = EnvUtil().get_env("NOSQL_DB_USER")
        self.db_password = EnvUtil().get_env("NOSQL_DB_USER_PASSWORD")
        self.db_name = EnvUtil().get_env("NOSQL_DB_DATABASE_NAME")

        self.max_msg_count = EnvUtil().get_env("MAX_MESSAGE_COUNT")

params = Params()
