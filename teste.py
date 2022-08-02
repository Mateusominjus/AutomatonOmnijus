
from json import dump
from automatonOmnijus import ConexaoCentral

central = ConexaoCentral(senha='omnijus01dev')
exemplo = central.ambiente('exemplo')

p2 = exemplo.processo(3)
p2.excluir()
