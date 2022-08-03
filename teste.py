
from json import dump
from automatonOmnijus import ConexaoCentral

central = ConexaoCentral(senha='omnijus01dev')
exemplo = central.ambiente('exemplo')
p1 = exemplo.processo('1',carregar=True)
p1.novo_documento('teste21.png')

