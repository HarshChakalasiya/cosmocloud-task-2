

nosql_client = AsyncIOMotorClient(f'mongodb+srv://{settings.cluster_user}:{settings.cluster_password}@{settings.cluster_name}/{settings.cluster_db_name}?retryWrites=true&w=majority')
nosql_engine = AIOEngine(motor_client=nosql_client,
                             database=settings.cluster_db_name)