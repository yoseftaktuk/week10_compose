import mysql.connector

class Sql_manager:
    def __init__(self):
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123"
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
        
        
    def insert(self, sql,val):
        mycursor = self.db.cursor()
        mycursor.execute(sql,val)
        self.db.commit()
        
        
    def close(self):
        self.db.close()
