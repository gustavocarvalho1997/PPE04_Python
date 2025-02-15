from sqlmodel import SQLModel, Field
from enums import Bancos, Status
from connection import engine


class Conta(SQLModel, table=True):
    id: int = Field(primary_key=True)
    valor: float
    banco: Bancos = Field(default=Bancos.NUBANK)
    status: Status = Field(default=Status.ATIVO)

if __name__ == "__main__":
    SQLModel.metadata.create_all(engine)