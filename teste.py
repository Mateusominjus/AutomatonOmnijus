
from json import dump
from automatonOmnijus import ConectCentral


central = ConectCentral(senha='omnijus01dev')
empresa = central.empresa('miojo')
em_erro = empresa.acoes_em_erro()
print(em_erro)