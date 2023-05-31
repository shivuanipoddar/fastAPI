def car_serializer(car) -> dict:
    return {
        "id": str(car["_id"]),
        "name": car["name"],
        "description": car["description"],
        "model": car["model"],
        "price": car["price"],
        "company": car["company"]
    }


def cars_list(cars) -> list:
    return [car_serializer(car) for car in cars]