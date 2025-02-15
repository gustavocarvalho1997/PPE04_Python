import matplotlib.pyplot as plt
from sqlmodel import Session, select
from models import Conta, Historico
from connection import engine
from enums import Bancos, Status, Tipos
from datetime import date, timedelta

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

def transferir_saldo(conta_origem, conta_destino, valor):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id == conta_origem)
        conta_origem = session.exec(statement).first()

        statement = select(Conta).where(Conta.id == conta_destino)
        conta_destino = session.exec(statement).first()

        if conta_origem.valor < valor:
            raise ValueError("Saldo insuficiente")

        conta_origem.valor -= valor
        conta_destino.valor += valor
        session.commit()

def movimentar_dinheiro(historico: Historico):
    with Session(engine) as session:
        statement = select(Conta).where(Conta.id == historico.conta_id)
        conta = session.exec(statement).first()

        if conta.status == Status.INATIVO:
            raise ValueError("Conta inativa")

        print(historico.tipos)

        if historico.tipos == Tipos.ENTRADA:
            conta.valor += historico.valor
        
        if historico.tipos == Tipos.SAIDA:
            if conta.valor < historico.valor:
                raise ValueError("Saldo insuficiente")
            conta.valor -= historico.valor 
        
        session.add(historico)
        session.commit()
        return historico
    
def total_contas():
    with Session(engine) as session:
        statement = select(Conta)
        contas = session.exec(statement).all()
        total = 0
        for conta in contas:
            total += conta.valor
    return float(total)

def buscar_historicos_entre_datas(data_inicio: date, data_fim: date):
    with Session(engine) as session:
        statement = select(Historico).where(
            Historico.data >= data_inicio,
            Historico.data <= data_fim
        )
        result = session.exec(statement).all()
    return result

def criar_grafico_por_conta():
    with Session(engine) as session:
        statement = select(Conta).where(Conta.status == Status.ATIVO)
        contas = session.exec(statement).all()
        labels = [conta.banco.value for conta in contas]
        valores = [conta.valor for conta in contas]
        plt.bar(labels, valores)
        plt.show()