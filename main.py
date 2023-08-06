from fastapi import FastAPI
from database import Base, engine
from api.v1.endpoints import images, prompts, sd_vars

Base.metadata.create_all(bind=engine)  # 创建数据库表

app = FastAPI()

app.include_router(images.router)
app.include_router(prompts.router)
app.include_router(sd_vars.router)
