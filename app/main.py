from fastapi import FastAPI
from .database import engine, Base
from .exceptions import CustomExceptionA, CustomExceptionB
from fastapi.exceptions import RequestValidationError
from .error_handlers import (
    custom_exception_a_handler,
    custom_exception_b_handler,
    validation_exception_handler
)
from .routers import task_10_1, task_10_2

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Контрольная работа №4",
    description="Технологии разработки серверных приложений",
    version="1.0.0"
)

app.add_exception_handler(CustomExceptionA, custom_exception_a_handler)
app.add_exception_handler(CustomExceptionB, custom_exception_b_handler)
app.add_exception_handler(RequestValidationError, validation_exception_handler)

app.include_router(task_10_1.router)
app.include_router(task_10_2.router)

@app.get("/")
async def root():
    return {
        "message": "Контрольная работа №4",
        "tasks": {
            "9.1": "Миграции (task_9_1.py)",
            "10.1": "/task10_1/check-condition?value=X",
            "10.2": "/task10_2/user (POST)"
        }
    }

@app.get("/health")
async def health():
    return {"status": "ok"}