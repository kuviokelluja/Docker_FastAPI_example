from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    ALLOWED_HOSTS: str = '"127.0.0.1", "localhost"'

    # Logger
    LOG_LEVEL = "DEBUG"
    JSON_LOGS = False

    # Env
    environment = os.environ.get("APIENV", "dev")

    if "production" in environment:
        openapi_url = ""
    else:
        openapi_url = "/openapi.json"

    # Version
    version = "0.0.1"
