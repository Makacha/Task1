from fastapi import FastAPI
from app.routers import api
from app.util import exception_handler, MyException
from uvicorn import run

app = FastAPI()
app.include_router(api.router)
app.add_exception_handler(MyException, exception_handler)

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8000)
