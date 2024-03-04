from fastapi import FastAPI
import uvicorn

from controller.probability import router as probability_router

app = FastAPI()

app.include_router(probability_router)