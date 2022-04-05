from typing import Set
import uvicorn
import sys
import logging
from loguru import logger
from api.api import app
from api.api import Settings
from api.utils import InterceptHandler

settings = Settings()
intercept_handler = InterceptHandler()
logging.root.setLevel(settings.LOG_LEVEL)


def configure_logger():
    seen: Set[str] = set()
    for name in [
        *logging.root.manager.loggerDict.keys(),
        "uvicorn",
        "uvicorn.access",
        "uvicorn.error",
    ]:
        if name not in seen:
            seen.add(name.split(".")[0])
            logging.getLogger(name).handlers = [intercept_handler]

    logger.configure(
        handlers=[
            {
                "sink": sys.stdout,
                "serialize": settings.JSON_LOGS,
                "level": settings.LOG_LEVEL,
            },
            {
                "sink": "logs/api.log",
                "serialize": settings.JSON_LOGS,
                "level": settings.LOG_LEVEL,
                "rotation": "03:00",
                "enqueue": True,
            },
        ]
    )


def start_server():
    configure_logger()
    runner()

def runner():
    uvicorn.run(
        "api.api:app",
        host="0.0.0.0",
        port=9999,
        reload=False,
        log_level=settings.LOG_LEVEL.lower(),
    )


if __name__ == "__main__":
    start_server()
