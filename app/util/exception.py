from fastapi.responses import JSONResponse


class MyException(Exception):
    code: int
    message: str

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message


def exception_handler(a, e):
    return JSONResponse(content={
        "error": e.code,
        "error_message": e.message
    }
    )
