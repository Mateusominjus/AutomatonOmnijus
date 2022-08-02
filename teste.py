
from json import dump
from automatonOmnijus import ConexaoCentral

central = ConexaoCentral(senha='omnijus01dev')
exemplo = central.ambiente('exemplo')

p2 = exemplo.processo(1)
p2.carregar_processo()
r = p2.documentos[0].baixar_binario_do_documento()
print(r.__class__)
with open('teste2.pdf','wb') as arq:
    arq.write(r)