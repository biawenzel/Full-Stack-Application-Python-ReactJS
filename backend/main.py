from typing import Union, List

from fastapi import FastAPI
from pydantic import BaseModel

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

@app.get("/api")
def read_root():
    return DB
