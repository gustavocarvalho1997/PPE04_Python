from sqlmodel import Session, select
from models import Conta
from connection import engine
from enums import Bancos, Status

def criar_conta(conta: Conta):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.banco == conta.banco)
        result = session.exec(statement).all()
        if result:
            print(f"Conta do banco {conta.banco.value} já existe")
            return
        session.add(conta)
        session.commit()
        return conta
    
def listar_contas():
    with Session(engine) as session:
        statement = select(Conta)
        result = session.exec(statement).all()
    return result

def desativar_conta(id):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id == id)
        conta = session.exec(statement).first()

        if conta.valor > 0:
            raise ValueError("Conta com saldo positivo não pode ser desativada")
        
        conta.status = Status.INATIVO
        session.commit()

# conta = Conta(valor=0, banco=Bancos.ITAU)
# criar_conta(conta)
# print(listar_contas())
desativar_conta(3)