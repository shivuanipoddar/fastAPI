from fastapi import FastAPI, HTTPException
from app.db.model import Car
from app.schemas.schemas import cars_list
from pymongo import MongoClient
from bson import ObjectId

mongodb_client = MongoClient("mongodb://localhost:27017/fastApi_db")

db = mongodb_client["cars"]
app = FastAPI()


@app.get("/car")
def get_all_car():
    car = cars_list(db["car"].find())
    return {"status": "ok", "data": car}


@app.get("/car/id")
def get_car(id: str):
    car = cars_list(db["car"].find({"_id": ObjectId(id)}))
    return {"status": "ok", "data": car}


@app.post("/car")
def create_car(car: Car):
    car = db["car"].insert_one(dict(car))
    return {"status": "ok", "data": car}


@app.put("/car/id")
def update_car(id: str, car: Car):
    car = db["car"].find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(car)})
    return {"status": "ok", "data": car}


@app.delete("/car/id")
def delete_car(id: str, car: Car):
    car = db["car"].find_one_and_delete({"_id": ObjectId(id)})
    return {"status": "ok", "data": car}

