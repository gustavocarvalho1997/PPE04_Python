from enum import Enum

class Bancos(Enum):
    NUBANK = "Nubank"
    ITAU = "Itaú"
    BRADESCO = "Bradesco"
    SANTANDER = "Santander"
    INTER = "Inter"
    CAIXA = "Caixa"
    BANCO_DO_BRASIL = "Banco do Brasil"

class Status(Enum):
    ATIVO = "Ativo"
    INATIVO = "Inativo"