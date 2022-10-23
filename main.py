import psycopg2
from config import user, password, db_name, host

# CREATE DATABASE
try:
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    connection.autocommit = True

    with connection.cursor() as cursor:
        cursor.execute('SELECT version();')
        print(f'SERVER VERSION {cursor.fetchone()}')


    class CreateTable:
        def __init__(self, table):
            self.table = table

        def create_table(self):
            with connection.cursor() as cursor:
                cursor.execute(self.table)
                # CREATE TABLE user(id serial PRIMARY KEY,name varchar(50)...);


    class DropTable:
        def __init__(self, *table_name):
            self.table_name = table_name

        def delete_table(self):
            with connection.cursor() as cursor:
                cursor.execute(f'DROP TABLE {self.table_name}')
                # DROP TABLE <name_table>;


    class InsertData:
        def __init__(self, table_name, data):
            self.table_name = table_name
            self.data = data

        def insert_data(self):
            with connection.cursor() as cursor:
                cursor.execute(f'INSERT INTO {self.table_name} VALUES({self.data});')
                # INSERT INTO user VALUES(1,'Kirill');


    class Select:
        def __init__(self, select):
            self.select = select

        def selectData(self):
            with connection.cursor() as cursor:
                cursor.execute(f' ')

    pt = DropTable(input())
    pt.delete_table()


except Exception as error:
    print('Error while working PostgreSQL', error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('INFO PostgreSQL connection closed')
