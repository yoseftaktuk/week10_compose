import mysql.connector
from dotenv import load_dotenv
import os
from sql import 

load_dotenv()

class Sql_manager:
    def __init__(self):
        self.db = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv("DB_USER"),
        password=os.getenv('DB_PASSWORD'),
        port=1433,
        )


    def select(self,sql): 
        mycursor = self.db.cursor()
        mycursor.execute(sql)
        myresult = mycursor.fetchall()      
        return myresult

    
    def update(self, sql):
        mycursor = self.db.cursor()
        mycursor.execute(sql)
        self.db.commit()
        
        
    def insert(self, sql, val):
        mycursor = self.db.cursor()
        mycursor.execute(sql,val)
        self.db.commit()
        
        
    def close(self):
        self.db.close()


a = Sql_manager()
a.insert('INSERT INTO chip (id, deposit) VALUES (%s, %s);',('1', '100'))