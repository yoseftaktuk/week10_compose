from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel, Field
import data_interactor
from contact import Contact


app = FastAPI()

class Item(BaseModel):
    id : int | None = Field(default=None)
    first_name: str
    last_name: str
    phone_number: str


cruser = data_interactor.Sql_manager()

@app.get('/contacts')
def get_all_contacts():
    data = cruser.select('SELECT * FROM contacts')
    conects = Contact(data)
    return conects.convert_to_dict()
    


@app.post('/contacts')
def create_contact(item: Item):

    try:
        sql = "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)"
        val = (item.first_name, item.last_name, item.phone_number)
        cruser.send_sql(sql=sql, val=val)
        return {'The sending was successful.'}
    except ConnectionError:
        return {'post faild'}

@app.put('/contacts/')
def update_contact(item: Item, id: int):
    try:
        sql = f"UPDATE contacts SET first_name = %s, last_name = %s, phone_number = %s WHERE id = %s;"
        val = (item.first_name, item.last_name, item.phone_number, id)
        cruser.send_sql(sql=sql, val=val)
        return {'The sending was successful.'} 
    except ConnectionError:
        return {'UPDATE faild'}


@app.delete('/contacts/')
def delete_contact(id: int):
    try:
        sql = f"DELETE FROM contacts WHERE id = {id}"
        cruser.execute(sql=sql)
        return {'The deletion was successful'}
    except ConnectionError:
        return {'DELETE faild'}

if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000,reload=True)