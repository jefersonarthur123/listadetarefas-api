from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.tarefa import TarefaCreate, TarefaUpdate, TarefaResponse
from app.services.tarefa_service import TarefaService

router = APIRouter(prefix="/api/tarefas", tags=["Tarefas"])

def get_tarefa_service(db: Session = Depends(get_db)) -> TarefaService:
    return TarefaService(db)

@router.get("", response_model=list[TarefaResponse], summary="Listar todas as tarefas")
def listar_tarefas(service: TarefaService = Depends(get_tarefa_service)):
    return service.listar_todas()

@router.get("/{id}", response_model=TarefaResponse, summary="Buscar tarefa por ID")
def buscar_tarefa(id: int, service: TarefaService = Depends(get_tarefa_service)):
    return service.buscar_por_id(id)

@router.post("", response_model=TarefaResponse, status_code=status.HTTP_201_CREATED, summary="Criar nova tarefa")
def criar_tarefa(tarefa_in: TarefaCreate, service: TarefaService = Depends(get_tarefa_service)):
    return service.criar(tarefa_in)

@router.put("/{id}", response_model=TarefaResponse, summary="Atualizar tarefa existente")
def atualizar_tarefa(id: int, tarefa_in: TarefaUpdate, service: TarefaService = Depends(get_tarefa_service)):
    return service.atualizar(id, tarefa_in)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, summary="Deletar tarefa por ID")
def deletar_tarefa(id: int, service: TarefaService = Depends(get_tarefa_service)):
    service.deletar(id)