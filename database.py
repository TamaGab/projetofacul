import mysql.connector

def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="gordoidiota123",
        database="faculdade"
    )

