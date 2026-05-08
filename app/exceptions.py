from fastapi import HTTPException

class CustomExceptionA(HTTPException):
    def __init__(self, detail: str = "Условие не выполнено"):
        super().__init__(status_code=400, detail=detail)

class CustomExceptionB(HTTPException):
    def __init__(self, detail: str = "Ресурс не найден"):
        super().__init__(status_code=404, detail=detail)