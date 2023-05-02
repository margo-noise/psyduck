import uvicorn
from fastapi import FastAPI
from core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)