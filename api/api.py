from typing import Any, Dict
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from api.config import Settings

settings = Settings()
app = FastAPI(version=settings.version, openapi_url=settings.openapi_url)


@app.get("/")
async def root() -> HTMLResponse:
    html = """
    <html>
        <head>
            <title>Title</title>
        </head>
        <body>
            <h1>Hello World!</h1>
        </body>
    </html>
    """
    return HTMLResponse(html, 200)
