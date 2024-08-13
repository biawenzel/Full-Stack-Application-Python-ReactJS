from typing import Union, List
from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class Person(BaseModel):
    id: int
    name: str
    age: int

DB: List[Person] = [
    Person(id=1, name="Alice", age=24),
    Person(id=2, name="Bob", age=27),
    Person(id=3, name='Beatriz', age=31)
]

@app.get("/api01")
def read_root():
    return DB

@app.get("/api02")
def read_json():
    with open("data.json", "r") as file:
        data = json.load(file)
    return data