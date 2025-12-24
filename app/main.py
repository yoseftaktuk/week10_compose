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
    print('5678')
    data = cruser.select('SELECT * FROM contacts')
    conects = Contact(data)
    return conects.convert_to_dict()
    


@app.post('/contacts')
def create_contact(item: Item):

    try:
        #cruser.execute(f"INSERT INTO contacts (first_name, last_name, phone_number) VALUES ({item.first_name}, {item.last_name}, {item.phone_number})")
        sql = "INSERT INTO customers (name, address) VALUES (%s, %s, %s)"
        val = (item.first_name, item.last_name, item.phone_number)
        cruser.test(sql=sql, val=val)
        return {'The sending was successful.'}
    except ConnectionError:
        return {'post faild'}

@app.put('/contacts/4')
def update_contact(item: Item):
    try:
        cruser.execute(f"UPDATE contacts set first_name = {item.first_name}, last_name = {item.last_name}, phone_number = {item.phone_number}  WHERE id = {item.id};")
        return {'The sending was successful.'} 
    except ConnectionError:
        return {'UPDATE faild'}


@app.delete('/contacts/4')
def delete_contact(id):
    try:
        cruser.execute(f"DELETE FROM table_name WHERE {id};")
        return {'The deletion was successful'}
    except ConnectionError:
        return {'DELETE faild'}

if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000,reload=True)