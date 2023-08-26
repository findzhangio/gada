# celery_app.py
from celery import Celery
from service.image import generate_and_store_image
from contextlib import contextmanager
from db import database
from os import environ
from config import Config

celery_app = Celery(
    "fastapi_app",
    broker=Config.REDIS_URL,  # 使用Redis作为消息代理
)


@contextmanager
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@celery_app.task
def task_generate_and_store_image(sd_var_id, sd_prompt_id):
    # 确保你有适当的错误处理和日志记录
    try:
        with get_db() as db:
            generate_and_store_image(sd_prompt_id, sd_var_id, db)
    except Exception as e:
        print(f"Error when generating image: {e}")


celery_app.conf.task_routes = {
    "task_generate_and_store_image": "main-queue",
}
