from util.config import params


class Util:

    @staticmethod
    def get_database_url():
        return f"mongodb://{params.db_user}:" \
               f"{params.db_password}@" \
               f"{params.db_host}:" \
               f"{params.db_port}/{params.db_name}"
