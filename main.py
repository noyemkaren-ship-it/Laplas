import uvicorn
from fastapi import FastAPI
from routers import (
    routers
)
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Laplas")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

for rout in routers:
    app.include_router(rout)


if __name__ == "__main__":
    """ Запуск программы """
    uvicorn.run(app, port=7600)
