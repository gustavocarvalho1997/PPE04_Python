from sqlmodel import SQLModel, Field, Relationship
from enums import Bancos, Status, Tipos
from connection import engine
from datetime import date


class Conta(SQLModel, table=True):
    id: int = Field(primary_key=True)
    valor: float
    banco: Bancos = Field(default=Bancos.NUBANK)
    status: Status = Field(default=Status.ATIVO)

    def __str__(self):
        return f"Conta {self.banco.value} - {self.valor} - {self.status.value}"
    
class Historico(SQLModel, table=True):
    id: int = Field(primary_key=True)
    conta_id: int = Field(foreign_key="conta.id")
    conta: Conta = Relationship()
    tipos: Tipos = Field(default=Tipos.ENTRADA)
    valor: float
    data: date

if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)