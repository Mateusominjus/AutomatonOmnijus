
from json import dump
from automatonOmnijus import ConectCentral


central = ConectCentral(senha='omnijus01dev')
empresa = central.empresa('boa_vista')
r = empresa.todos_processos()
print(r)
