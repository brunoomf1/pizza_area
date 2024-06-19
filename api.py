import fastapi
from lib.libarea import *
from lib.libdb import *
from lib.libquerydb import *
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi


log

app = fastapi.FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000"
]

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Your API Title",
        version="1.0.0",
        description="Your API description",
        routes=app.routes,
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Wellcome to pizza_area API"}

@app.post('/pizza_area')
async def area(diameter: int, n_people: int):
    p_area = pizza_area()
    p_area.configure(diameter,n_people)
    p_area.process()
    n_people,area,diameter,n_slice = p_area.get_pizza_info()
    return {"n_people": n_people, "area": area, "diameter": diameter, "n_slice": n_slice}

@app.get('/pizza_places')
async def pizza_places():
    pizza_places = getAllPlaces('')
    return pizza_places

@app.get('/pizza_places/{uf}')
async def uf(uf:str):
    pizza_places = getAllPlaces(uf=uf)
    return pizza_places