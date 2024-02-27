# Factory method
# env var depending

class DbConnector:

    @classmethod
    def get_db_connector(cls, current_env):
        _connectors = {
            'dev': cls.get_mongo_db_connector(),
            'prod': cls.get_postgres_db_connector(),
        }
        return _connectors.get(current_env, 'There is no connector')

    @staticmethod
    def get_mongo_db_connector():  # dev
        connector = 'MongoDB_conn'
        return connector

    @staticmethod
    def get_postgres_db_connector():  # prod
        connector = 'Postgres_conn'
        return connector


if __name__ == '__main__':
    import os
    print(DbConnector.get_db_connector(os.getenv('CURRENT_ENV')))
    print(os.environ)