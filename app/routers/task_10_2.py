from fastapi import APIRouter
from ..schemas import UserCreate, UserResponse

router = APIRouter(prefix="/task10_2", tags=["Задание 10.2"])

@router.post("/user", response_model=UserResponse, status_code=201)
async def create_user(user: UserCreate):
    return UserResponse(
        id=1,
        username=user.username,
        age=user.age,
        email=user.email,
        phone=user.phone
    )

@router.get("/user/example")
async def get_example():
    return {
        "example": {
            "username": "ivan_ivanov",
            "age": 25,
            "email": "ivan@example.com",
            "password": "Secure123",
            "phone": "+79001234567"
        }
    }