from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Tarefa(Base):
    __tablename__ = "tb_tarefas"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    descricao: Mapped[str] = mapped_column(String(255), nullable=False)
    concluida: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)