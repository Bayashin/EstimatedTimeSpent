from fastapi import FastAPI
from .controller.root import router as root_router
from .controller.probability import router as probability_router

app = FastAPI()

app.include_router(root_router)
app.include_router(probability_router)