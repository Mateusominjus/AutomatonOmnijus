
from automatonOmnijus import ConectCentral


central = ConectCentral(senha='omnijus01')
empresa = central.empresa('miojo')
processo = empresa.processo(1)
r = processo.dados_do_processo()
print(r)