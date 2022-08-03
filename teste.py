
from json import dump
from automatonOmnijus import ConexaoCentral

central = ConexaoCentral(senha='omnijus01dev')
exemplo = central.ambiente('exemplo')
p1 = exemplo.processo('1').criar_processo()
p1
r = p1.excluir_processo()
print(r)