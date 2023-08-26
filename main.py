# main.py
from fastapi import FastAPI
from db.database import Base, engine
from api.v1.endpoints import images, prompts, sd_vars, image_tasks
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from config import Config

Base.metadata.create_all(bind=engine)  # 创建数据库表

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=Config.CORS_ALLOW_ORIGINS,
    allow_credentials=Config.CORS_ALLOW_CREDENTIALS,
    allow_methods=Config.CORS_ALLOW_METHODS,
    allow_headers=Config.CORS_ALLOW_HEADERS,
)


app.include_router(images.router)
app.include_router(prompts.router)
app.include_router(sd_vars.router)
app.include_router(image_tasks.router)


if __name__ == "__main__":
    host = "0.0.0.0"
    port = Config.PORT
    print(f"Running on http://{host}:{port}")
    uvicorn.run("main:app", host=host, port=port, reload=True)
