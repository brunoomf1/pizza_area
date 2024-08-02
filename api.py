# Copyright (c) 2024, Bruno Monteiro
# All rights reserved.

import fastapi
from lib.libarea import *
from lib.libdb import *
from lib.libquerydb import *
from lib.libutils import *
from lib.libmodels import *
from lib.liblog import *
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from typing import Literal, Optional

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
async def area(diameter: int, n_people: int):
    p_area = pizza_area()
    p_area.configure(diameter, n_people)
    p_area.process()
    n_people, area, diameter, n_slice = p_area.get_pizza_info()
    return {"n_people": n_people, "area": area, "diameter": diameter, "n_slice": n_slice}

@app.get('/pizza_places')
async def pizza_places():
    pizza_places = getAllPlaces('')
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
async def ufs_by_option(
    uf: ufsModels
):
    response = get_uf(uf=uf)
    response = translateListToJson(ufs)
    return response
