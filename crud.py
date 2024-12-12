
print("--------------------------Go!----------------------------------")
'''
CRUD

CREATE
READ
UPDATE
DELETE

'''
#Step 1- Install MySQL Driver - pip install mysql-connector-python
#Step 2- Use import mysql.connector
#Step 3- Open MySQL Workbench 
#Step 4- Create Database and Table
#Step 5- Create Connection
#Step 6- Create Cursor

from datetime import date
from datetime import datetime

data_atual = date.today()
horario = datetime.now().time()
print(f"Now {horario} .Today is {data_atual}.\n")


import mysql.connector

connectionMySQL = mysql.connector.connect(
    host='localhost',
    user='root',
    password='@Prff03011991',
    database='database',
)

cursor = connectionMySQL.cursor()


cursor.close()
connectionMySQL.close()

'''
import mysql.connector

# Conexão com o banco de dados
try:
    connection= mysql.connector.connect(
        host="localhost",               # Endereço do servidor (ou IP)
        user="root",                    # Usuário do banco de dados
        password="@Prff03011991",       # Senha do usuário
        database="meubanco"             # Nome do banco de dados
    )

    if connection.is_connected():
        print("Conexão bem-sucedida!")
        print(f"Servidor: {connection.get_server_info()}")

except mysql.connector.Error as e:
    print(f"Erro ao conectar ao MySQL: {e}")

finally:
    if connection.is_connected():
        connection.close()
        print("Conexão encerrada.")
'''


























print("/n--------------------------Stop!---------------------------------")
