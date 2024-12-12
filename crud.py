
print("/n--------------------------Go!----------------------------------")
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

'''
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

from datetime import date
from datetime import datetime

data_atual = date.today()
horario = datetime.now().time()
print(f"Now {horario} .Today is {data_atual}.")


























print("/n--------------------------Stop!---------------------------------")
