
from json import dump
from automatonOmnijus import ConectCentral


central = ConectCentral(senha='omnijus01dev')
empresa = central.empresa('boa_vista')
x = empresa.excluir_todos_processos()
