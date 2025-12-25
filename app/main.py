from fastapi import FastAPI , HTTPException
import uvicorn
from pydantic import BaseModel, Field
from data_interactor import Contact
import data_interactor 

app = FastAPI()

class Item(BaseModel):
    id : int | None = Field(default=None)
    first_name: str
    last_name: str
    phone_number: str

qury = data_interactor.DatabaseService()


@app.get('/contacts')
def get_all_contacts():
    return qury.get_all_contacts()


@app.post('/contacts')
def create_contact(item: Item):
    my_item = data_interactor.Contact(item)
    item = my_item.convert_to_dict()
    return qury.create_contact(item)

@app.put('/contacts/')
def update_contact(item: Item, id: int):
    my_item = data_interactor.Contact(item)
    item = my_item.convert_to_dict()
    return qury.update_contact(id, item)


@app.delete('/contacts/')
def delete_contact(id: int):
    return qury.delete_contact(id)

if __name__ == "__main__":
    uvicorn.run('main:app', host="0.0.0.0", port=8000,reload=True)