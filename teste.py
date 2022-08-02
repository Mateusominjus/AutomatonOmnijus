
from json import dump
from automatonOmnijus import ConexaoCentral

central = ConexaoCentral(senha='omnijus01dev')
exemplo = central.ambiente('exemplo')
p1 = exemplo.processo(1).carregar_processo()
doc = p1.documento(nome='carta_porsche.pdf')
print(doc)