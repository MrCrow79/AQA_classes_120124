# Singleton
# db connector


class DynamoDBConnectionMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if not cls._instances.get(cls):
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]


import os


class DynamoDBConnection(metaclass=DynamoDBConnectionMeta):

    def __init__(self):
        self.user_name = os.environ.get('db_user')
        self.user_password = os.environ.get('db_password')
        self.host = os.environ.get('db_host')
        self.table_companies = 'dev-companies'
        self.table_prices = 'dev-prices'
        self.connection = None

    def set_connection(self):
        self.connection = 'connection'

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def get_company_name(self):
        pass


class TestCompanies:

    db_dynamo = DynamoDBConnection()

    def test_companies(self):
        name = 'Com1'
        assert name == self.db_dynamo.get_company_name()


def tear_down():
    db_dynamo = DynamoDBConnection()
    db_dynamo.close_connection()


dynamo_1 = DynamoDBConnection()
dynamo_2 = DynamoDBConnection()


dynamo_1.test_var = 2
print(dynamo_1.host)
print(dynamo_2.host)

print(dynamo_1 is dynamo_2)  # первіряє чи є 2 об'єкти один і тим самим(перевіряє id)
print(id(dynamo_1))
print(id(dynamo_2))


