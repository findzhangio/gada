# config.py
from os import environ


def get_env_to_list(env_var, default=None):
    if default is None:
        default = []
    envs = environ.get(env_var)
    if not envs:
        return default

    if "," in envs:
        return envs.split(",")

    return [envs]


class Config:
    DEBUG = environ.get('DEBUG', False)
    PORT = int(environ.get('PORT', 8080))
    MYSQL_URL = environ.get("MYSQL_URL")
    REDIS_URL = environ.get("REDIS_URL")
    OPENAI_API_KEY = environ.get("OPENAI_API_KEY")
    SD_WEBUI_HOST = environ.get("SD_WEBUI_HOST")
    SD_WEBUI_PORT = environ.get("SD_WEBUI_PORT")
    COS_SECRET_ID = environ.get("COS_SECRET_ID")
    COS_SECRET_KEY = environ.get("COS_SECRET_KEY")
    COS_REGION = environ.get("COS_REGION")
    COS_BUCKET = environ.get("COS_BUCKET")
    CONSUMER_KEY = environ.get("CONSUMER_KEY")
    CONSUMER_SECRET = environ.get("CONSUMER_SECRET")
    ACCESS_TOKEN = environ.get("ACCESS_TOKEN")
    ACCESS_TOKEN_SECRET = environ.get("ACCESS_TOKEN_SECRET")
    BEARER_TOKEN = environ.get("BEARER_TOKEN")
    CORS_ALLOW_ORIGINS = get_env_to_list("CORS_ALLOW_ORIGINS", ['*'])
    CORS_ALLOW_METHODS = get_env_to_list("CORS_ALLOW_METHODS", ['GET', 'POST', 'PUT', 'DELETE'])
    CORS_ALLOW_HEADERS = get_env_to_list("CORS_ALLOW_HEADERS", ['Content-Type'])
    CORS_ALLOW_CREDENTIALS = get_env_to_list("CORS_ALLOW_CREDENTIALS", [True])
    COS_IMAGE_PATH = environ.get("COS_IMAGE_PATH", '/sd/')
    IMAGE_CACHE_PATH = environ.get("IMAGE_CACHE_PATH", './tmp/')

