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
        def __init__(self, table_name):
            self.table_name = table_name

        def delete_table(self):
            with connection.cursor() as cursor:
                cursor.execute(f'DROP TABLE {self.table_name}')
                # DROP TABLE <name_table>;


    class InsertData:
        def __init__(self, table_name, *words):
            self.table_name = table_name
            self.words = words

        def insert_data(self):
            with connection.cursor() as cursor:
                cursor.execute(f'INSERT INTO {self.table_name} VALUES({self.words});')
                # INSERT INTO user VALUES(1,'Kirill');


    class Select:
        def __init__(self, sel):
            self.select = sel

        def selectData(self):
            with connection.cursor() as cursor:
                cursor.execute(f'SELECT {self.select}')


    n = int(input('Введите действие которое хотите выбрать\n'
                  '1)Создание таблицы\n'
                  '2)Удаление таблицы\n'
                  '3)Вставка\n'
                  '4)Запрос\n'
                  '5)Чтобы выйти из таблицы наберите на клавиатуре число больше 4'))

    while True:
        if n == 1:
            table = input('Создайте таблицу с помощью SQL кода')
            pt = CreateTable(table)
            pt.create_table()
            break
        elif n == 2:
            drop = input('Введите название таблицы для удаления или укажите таблицы через запятую')
            pt = DropTable(drop)
            pt.delete_table()
            break
        elif n == 3:
            name_table = input('Введите название таблицы')
            data = input('Введите данные для присвоения столбцам таблицы')
            pt = InsertData(name_table, data)
            pt.insert_data()
            break
        elif n == 4:
            select = input('Введите запрос без SELECT')
            pt = Select(select)
            pt.selectData()
            break
        else:
            print('Выход')
            break


except Exception as error:
    print('Error while working PostgreSQL', error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('INFO PostgreSQL connection closed')
