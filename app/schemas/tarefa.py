from pydantic import BaseModel, ConfigDict, Field

class TarefaBase(BaseModel):
    descricao: str = Field(..., min_length=1, max_length=255, description="Descrição da tarefa")
    concluida: bool = Field(default=False, description="Status de conclusão")

class TarefaCreate(TarefaBase):
    pass

class TarefaUpdate(BaseModel):
    descricao: str | None = Field(default=None, min_length=1, max_length=255)
    concluida: bool | None = Field(default=None)

class TarefaResponse(TarefaBase):
    id: int

    model_config = ConfigDict(from_attributes=True)         