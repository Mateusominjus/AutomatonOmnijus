
from json import dump
from automatonOmnijus import ConexaoCentral

central = ConexaoCentral(senha='omnijus01dev')
exemplo = central.ambiente('exemplo')
p1 = exemplo.processo(1,carregar=True)
doc = p1.novo_documento()
doc.fazer_upload_de_documento('teste1.png')