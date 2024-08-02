# Copyright (c) 2024, Bruno Monteiro
# All rights reserved.

import fastapi
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from typing import Literal, Optional

from lib.libarea import *
from lib.libdb import *
from lib.libquerydb import *
from lib.libutils import *
from lib.libmodels import *
from lib.liblog import *
from sbin.pEngine import *

app = fastapi.FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "https://pizza-area.vercel.app"
]


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Pizza Places",
        version="1.0.0",
        description="API destinada a calcular area de pizzas e obter uma listagem das pizzarias de SM",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return FileResponse("static/home.html")


@app.post('/pizza_area')
async def area(diameter: float, n_people: int):
    return eng_pizza_calculate(diameter, n_people)


@app.get('/pizza_places')
async def pizza_places():
    pizza_places = getAllPlaces()
    return pizza_places


@app.get('/pizza_places/{uf}')
async def pizza_places_by_uf(uf: str):
    pizza_places = getAllPlaces(uf=uf)
    return pizza_places


@app.get('/ufs/')
async def ufs():
    ufs = get_list_uf()
    response = translateListToJson(ufs)
    return response


ufsModels = UFsClass


@app.get('/ufs/{uf}')
async def ufs_by_option(uf: ufsModels):
    response = get_uf(uf=uf)
    response = translateListToJson(response)
    return response

