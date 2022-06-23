
from automatonOmnijus import ConectCentral


central = ConectCentral(senha='omnijus01')
empresa = central.empresa('miojo')
processo = empresa.processo(12)
print(processo.dados_do_processo())