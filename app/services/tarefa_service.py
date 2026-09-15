from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repositories.tarefa_repository import TarefaRepository
from app.schemas.tarefa import TarefaCreate, TarefaUpdate
from app.models.tarefa import Tarefa

class TarefaService:
    def __init__(self, db: Session):
        self.repository = TarefaRepository(db)

    def listar_todas(self) -> list[Tarefa]:
        return self.repository.find_all()

    def buscar_por_id(self, id: int) -> Tarefa:
        tarefa = self.repository.find_by_id(id)
        if not tarefa:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Tarefa não encontrada com o id: {id}",
            )
        return tarefa

    def criar(self, tarefa_in: TarefaCreate) -> Tarefa:
        return self.repository.create(tarefa_in)

    def atualizar(self, id: int, tarefa_in: TarefaUpdate) -> Tarefa:
        db_tarefa = self.buscar_por_id(id)
        return self.repository.update(db_tarefa, tarefa_in)

    def deletar(self, id: int) -> None:
        db_tarefa = self.buscar_por_id(id)
        self.repository.delete(db_tarefa)