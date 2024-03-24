from fastapi import FastAPI
from database import Base, engine, SessionLocal
import uvicorn

from routers.user import router as user_router

Base.metadata.create_all(bind = engine)

app = FastAPI(
    title = 'Alchemy Practic'
)
app.include_router(user_router)


if __name__ == "__main__":
    
    
    uvicorn.run("main:app", reload = True)