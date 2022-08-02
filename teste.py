
from json import dump
from automatonOmnijus import ConexaoCentral

central = ConexaoCentral(senha='omnijus01dev')
exemplo = central.ambiente('exemplo')
p1 = exemplo.processo(1,carregar=True)
doc = p1.documento('teste3.png')
doc.excluir()