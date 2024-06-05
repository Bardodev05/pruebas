from fastapi import APIRouter, HTTPException,status,FastAPI
from models.instrument import Instrument
router = APIRouter()

@router.get("/instrument/{id}", tags=["instruments"])
async def read_item(id: int):
    # Buscar el instrumento por ID
    instrument = next((item for item in instruments_db if item.id == id), None)
    
    if instrument is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Instrumento con ID {id} no encontrado.")
    
    return instrument


@router.get("/instruments/",tags=["instruments"])
async def get_instruments():
    return instruments_db

@router.post("/instruments/", tags=["instruments"], response_model=Instrument)
async def create_instruments(instrument: Instrument):
    instruments_db.append(instrument)
    return instrument



@router.put("/instruments/{instrument_id}",tags=["instruments"])
async def update_instrument(instrument_id: int, instrument: Instrument):
    # Intentar encontrar el instrumento por ID
    found_instrument = next((item for item in instruments_db if item.id == instrument_id), None)
    
    if found_instrument is None:
        # Si el instrumento no se encuentra, lanzar una excepción personalizada
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"Instrumento con ID {instrument_id} no encontrado.")
    
    # Si el instrumento se encuentra, actualizar sus atributos
    found_instrument.name = instrument.name
    found_instrument.category = instrument.category
    found_instrument.description = instrument.description
    
    return found_instrument


@router.delete("/instruments/{instrument_id}",tags=["instruments"])
async def delete_instrument(instrument_id: int):
    # Declarar instruments_db como global al comienzo de la función
    global instruments_db
    
    # Copia de instruments_db para trabajar con ella
    instruments_db_copy = instruments_db.copy()
    
    # Buscar el instrumento por ID
    instrument_to_delete = next((item for item in instruments_db_copy if item.id == instrument_id), None)
    
    if instrument_to_delete is None:
        raise HTTPException(status_code=404, detail=f"Instrumento con ID {instrument_id} no encontrado.")
    
    # Eliminar el instrumento de la copia
    instruments_db_copy.remove(instrument_to_delete)
    
    # Actualizar instruments_db globalmente
    instruments_db = instruments_db_copy  # Ahora instruments_db se declara como global antes de ser modificada

    # Devolver los detalles del instrumento eliminado
    return {
        "detail": f"Instrumento con ID {instrument_id} eliminado.",
        "deleted_instrument": instrument_to_delete.model_dump()
    }
