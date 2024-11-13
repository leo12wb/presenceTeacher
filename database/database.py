import mysql.connector

def get_db_connection():
    connection = mysql.connector.connect(
        host='localhost',
        user='root',       # nome de usuário
        password='',   #  senha
        database='presenceTeacher' # Nome do banco de dados
    )
    return connection