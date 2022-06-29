
from json import dump
from automatonOmnijus import ConectCentral


central = ConectCentral(senha='omnijus01dev')
empresa = central.empresa('boa_vista')
x = empresa.criar_processo('00000000000000000003')
