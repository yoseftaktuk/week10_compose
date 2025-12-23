from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import data_interactor
from contact import Contact
app = FastAPI()

@app.get('/contacts')
def get_all_contacts():

    pass


@app.post('/contacts')
def create_contact(first_name, last_name, phone_number):
    data = data_interactor.Sql_manager.select('SELECT * FROM contact')
    conects = Contact(data)
    return conects.convert_to_dict()

@app.put('/contacts/4')
def update_contact(id, first_name, last_name, phone_number):
    pass

@app.delete('/contacts/4')
def delete_contact(id):
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)