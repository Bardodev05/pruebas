from fastapi import FastAPI
from models import Instrument
from routers.instrumentos_routers import instrumentos_routers


app = FastAPI()
app.title = "app de instrumentos"

app.include_router(instrumentos_routers)
# app.include_router()

instruments_db = [
    Instrument(id=1, name="cirrampla", category="1 Cuerda"),
    Instrument(id=2, name="ukulele", category="4 Cuerdas"),
    Instrument(id=3, name="banjo", category="5 Cuerdas"),
]

@app.get("/", tags=["Messeger"])
async def messeger():
    return {"message": "Hello World"}


