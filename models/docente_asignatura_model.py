from pydantic import BaseModel

class DocenteAsignatura(BaseModel):
    id: int = None
    id_docente: int
    nombre_docente: str | None = None
    id_asignatura: int
    nombre_asignatura: str | None = None