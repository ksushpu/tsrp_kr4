from fastapi import APIRouter, Query
from ..exceptions import CustomExceptionA, CustomExceptionB

router = APIRouter(prefix="/task10_1", tags=["Задание 10.1"])

fake_products = {
    1: {"id": 1, "name": "Ноутбук", "price": 999.99},
    2: {"id": 2, "name": "Мышь", "price": 29.99},
}

@router.get("/check-condition")
async def check_condition(value: int = Query(...)):
    if value <= 0:
        raise CustomExceptionA(detail=f"Значение {value} недопустимо. Должно быть > 0")
    return {"message": f"Значение {value} прошло проверку", "value": value}

@router.get("/product/{product_id}")
async def get_product(product_id: int):
    if product_id not in fake_products:
        raise CustomExceptionB(detail=f"Продукт с ID {product_id} не найден")
    return fake_products[product_id]

@router.get("/products")
async def list_products():
    return {"products": list(fake_products.values())}