from fastapi import Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from .exceptions import CustomExceptionA, CustomExceptionB
from .schemas import ErrorResponse

async def custom_exception_a_handler(request: Request, exc: CustomExceptionA):
    return JSONResponse(
        status_code=400,
        content=ErrorResponse(
            error_code="CUSTOM_A_ERROR",
            message=exc.detail,
            details="Проверьте входные данные"
        ).model_dump()
    )

async def custom_exception_b_handler(request: Request, exc: CustomExceptionB):
    return JSONResponse(
        status_code=404,
        content=ErrorResponse(
            error_code="CUSTOM_B_ERROR",
            message=exc.detail,
            details="Запрашиваемый ресурс не существует"
        ).model_dump()
    )

async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = []
    for error in exc.errors():
        errors.append({
            "field": error["loc"][-1],
            "message": error["msg"],
            "type": error["type"]
        })
    
    return JSONResponse(
        status_code=422,
        content=ErrorResponse(
            error_code="VALIDATION_ERROR",
            message="Ошибка валидации данных",
            details=str(errors)
        ).model_dump()
    )