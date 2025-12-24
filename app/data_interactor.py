import mysql.connector
from dotenv import load_dotenv
import os


class Contact:
    def __init__(self, contact_info: object):
        self.id = contact_info.id
        self.first_name = contact_info.first_name
        self.last_name = contact_info.last_name
        self.phone_number = contact_info.phone_number

    def convert_to_dict(self):
        return {"id": self.id, 
                "first_name": self.first_name, 
                "last_name": self.last_name, 
                "phone_number": self.phone_number}
    

class DatabaseService:

    def __init__(self):
        self.db = mysql.connector.connect(
            user=os.getenv('DB_USER'), 
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            database=os.getenv('DB_NAME')
            )

    def get_all_contacts(self: str): 
        mycursor = self.db.cursor()
        mycursor.execute('SELECT * FROM contacts')
        myresult = mycursor.fetchall()      
        return myresult
    
    def create_contact(self, item: dict):
        try:
            mycursor = self.db.cursor()
            sql = "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)"
            val = (item['first_name'], item['last_name'], item['phone_number'])
            mycursor.execute(sql, val)
            self.db.commit()
            return {'The sending was successful.'}
        except ConnectionError:
            return {'post faild'}
        
    def update_contact(self, id: int , item: dict):
        try:
            mycursor = self.db.cursor()
            sql = f"UPDATE contacts SET first_name = %s, last_name = %s, phone_number = %s WHERE id = %s;"
            val = (item['first_name'], item['last_name'], item['phone_number'], id)
            mycursor.execute(sql, val)
            self.db.commit()
            return {'The sending was successful.'} 
        except ConnectionError:
            return {'UPDATE faild'}
        
    def delete_contact(self, id):
        try:
            mycursor = self.db.cursor()
            sql = f"DELETE FROM contacts WHERE id = {id}"
            mycursor.execute(sql)
            return {'The deletion was successful'}
        except ConnectionError:
            return {'DELETE faild'}
