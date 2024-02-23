# from typing import Union
from fastapi import FastAPI
router = FastAPI()

import api.controller.root as root

@router.get("/")
def read_root():
    hello = root.Hello()
    return hello
