from sqlalchemy.orm import Session
from app.models.tarefa import Tarefa
from app.schemas.tarefa import TarefaCreate, TarefaUpdate


class TarefaRepository:
    def __init__(self, db: Session):
        self.db = db

    def find_all(self) -> list[Tarefa]:
        return self.db.query(Tarefa).order_by(Tarefa.id.asc()).all()

    def find_by_id(self, id: int) -> Tarefa | None:
        return self.db.query(Tarefa).filter(Tarefa.id == id).first()

    def create(self, tarefa_in: TarefaCreate) -> Tarefa:
        db_tarefa = Tarefa(
            descricao=tarefa_in.descricao,
            concluida=tarefa_in.concluida,
        )
        self.db.add(db_tarefa)
        self.db.commit()
        self.db.refresh(db_tarefa)
        return db_tarefa

    def update(self, db_tarefa: Tarefa, tarefa_in: TarefaUpdate) -> Tarefa:
        if tarefa_in.descricao is not None:
            db_tarefa.descricao = tarefa_in.descricao
        if tarefa_in.concluida is not None:
            db_tarefa.concluida = tarefa_in.concluida

        self.db.commit()
        self.db.refresh(db_tarefa)
        return db_tarefa

    def delete(self, db_tarefa: Tarefa) -> None:
        self.db.delete(db_tarefa)
        self.db.commit()