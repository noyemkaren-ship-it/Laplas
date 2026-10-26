import uvicorn
from fastapi import FastAPI
from routers import routers
from fastapi.staticfiles import StaticFiles

app = FastAPI(title="Laplas")
app.mount("/static", StaticFiles(directory="static"), name="static")

for rout in routers:
    app.include_router(rout)

if __name__ == "__main__":
    uvicorn.run(app, port=7600)