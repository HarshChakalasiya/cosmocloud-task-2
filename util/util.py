import uuid
from enum import Enum

from util.config import params


class Util:

    @staticmethod
    def get_database_url():
        @staticmethod
        def get_database_url():
            return f"mongodb://{params.db_user}:" \
                   f"{params.db_password}@" \
                   f"{params.db_host}:" \
                   f"{params.db_port}/{params.db_name}"

    def generate_random_id(self):
        return str(uuid.uuid4())

class ValidationRegex(Enum):
    EMAIL = "[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}"
