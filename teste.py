
from automatonOmnijus import ConectCentral


central = ConectCentral(senha='omnijus01')
empresa = central.empresa('miojo')
acoes_pendentes = empresa.acoes_pendentes()
print(acoes_pendentes)