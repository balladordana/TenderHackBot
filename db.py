import psycopg2
import config


def connect():
    connection = None
    try:
        db_params = {
            'database': config.database,
            'user': config.username,
            'password': config.password,
            'host': config.host,
            'port': config.port,
        }

        connection = psycopg2.connect(**db_params)
        print("Connection made to the PostgreSQL database")
        var_cur = connection.cursor()

        return connection, var_cur

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return None, None


def select_users():
    connection, cursor = connect()
    if connection and cursor:
        table_name = 'users'

        # Выполняем SQL-запрос
        query = f"SELECT tg_id FROM {table_name};"
        cursor.execute(query)

        # Получаем результаты
        result = cursor.fetchall()

        # Закрываем курсор и соединение
        cursor.close()
        connection.close()
        print("Connection closed to the PostgreSQL database")

        return result
    else:
        print("Error connecting to the database.")
        return []


def select_user(username):
    connection, cursor = connect()
    if connection and cursor:
        table_name = 'users'

        # Выполняем SQL-запрос
        query = f"SELECT tg_id FROM {table_name} WHERE username = %s;"
        cursor.execute(query, (username, ))

        # Получаем результаты
        result = cursor.fetchone()

        # Закрываем курсор и соединение
        cursor.close()
        connection.close()
        print("Connection closed to the PostgreSQL database")

        return result
    else:
        print("Error connecting to the database.")
        return []


