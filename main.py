from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

users = {}
numbers = {"+8880001": False, "+8880002": False}
gifts = [{"id":1,"name":"Sword","price":100}]

class Register(BaseModel):
    number: str

@app.post("/register")
def register(data: Register):
    if data.number not in numbers:
        return {"error": "number not allowed"}
    if numbers[data.number]:
        return {"error": "number used"}
    users[data.number] = {"stars": 1000, "role": "user"}
    numbers[data.number] = True
    return {"ok": True}

@app.get("/gifts")
def get_gifts():
    return gifts
