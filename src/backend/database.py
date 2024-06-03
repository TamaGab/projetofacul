import mysql.connector

def connect():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123",
        database="faculdadedb"
    )
    return connection

def get_cursor():
    # Estabelece a conexão com o banco de dados
    db_connection = connect()

    # Cria um cursor para executar consultas SQL
    cursor = db_connection.cursor()

    return db_connection, cursor

def close_connection(connection, cursor):
    # Fecha o cursor e a conexão com o banco de dados
    cursor.close()
    connection.close()
