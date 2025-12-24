import mysql.connector
from dotenv import load_dotenv
import os


load_dotenv()

class Sql_manager:
    def __init__(self):
        self.db = mysql.connector.connect(
            user=os.getenv('DB_USER'), 
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME')
            )
        

    def select(self,sql: str): 
        mycursor = self.db.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()      
        return myresult

    
    def execute(self, sql: str):
        mycursor = self.db.cursor()
        mycursor.execute(sql)
        self.db.commit()

    def send_sql(self, sql: str, val: tuple):
        mycursor = self.db.cursor()
        mycursor.execute(sql, val)
        self.db.commit()    

    def close(self):
        self.db.close()


a = Sql_manager()
# a.insert('INSERT INTO chip (id, deposit) VALUES (%s, %s);',('1', '100'))