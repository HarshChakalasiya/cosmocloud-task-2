from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

from util.config import params
from util.util import Util

nosql_client = AsyncIOMotorClient(Util().get_database_url())
nosql_engine = AIOEngine(client=nosql_client,database=params.db_name)