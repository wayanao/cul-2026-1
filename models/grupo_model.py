from pydantic import BaseModel

class Grupo(BaseModel):
    id:int=None
    id_periodo:int
    periodo:str|None=None
    id_jornada:int
    jornada:str|None=None
    codigo:str
    cupo:int
    estado:bool=None