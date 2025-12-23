from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()

@app.get('/contacts')
def get_all_contacts():
    pass


@app.post('/contacts')
def create_contact(first_name, last_name, phone_number):
    pass

@app.put('/contacts/4')
def update_contact(id, first_name, last_name, phone_number):
    pass

@app.delete('/contacts/4')
def delete_contact(id):
    pass


if __name__ == '__name__':
    pass