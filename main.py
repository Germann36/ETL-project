#Основной скрипт

import psycopg2
import datetime
from config import host, user, password, host, potr, source_csv

def insert_row():
    with psycopg2.connect(
        database = param_database,
        user = param_user,
        password = param_password,
        host = param_host,
        port = param_port
    ) as conn:
        print('[INFO] Подключение к БД выполнено')

        with conn.cursor() as cur:
            print('[INFO] Подключение к cursor выполнено')

            with open(source_csv, encoding='utf-8') as file:
                next(file)  # Пропускаем заголовок
                for row in file:
                    row = row.strip().split(";")
                    if row[2] == (datetime.datetime.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"):  # Импортием данные за вчерашний день
                        print('[INFO] Подключение к файлу выполнено. Добавлена строка:', row)
                        cur.execute("INSERT INTO sales (product, quantity, date) VALUES (%s, %s, %s)", (row[0], int(row[1]), row[2]))

        conn.commit() # Фиксируем изменения в базе данных

insert_row() # Вызываем функцию
