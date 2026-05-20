from pydantic import BaseModel

class DisponibilidadDocente(BaseModel):
    id:int=None
    id_docente:int
    nombre:str|None=None
    id_periodo:int
    periodo:str|None=None
    dia_semana:int
    hora_inicio:str
    hora_fin:str
    observacion:str|None=None