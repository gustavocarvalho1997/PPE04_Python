from enum import Enum

class Bancos(Enum):
    NUBANK = "Nubank"
    ITAU = "Itaú"
    BRADESCO = "Bradesco"
    SANTANDER = "Santander"
    INTER = "Inter"
    CAIXA = "Caixa"
    BANCO_DO_BRASIL = "Banco Do Brasil"

class Status(Enum):
    ATIVO = "Ativo"
    INATIVO = "Inativo"

class Tipos(Enum):
    ENTRADA = 'Entrada'
    SAIDA = 'Saida'