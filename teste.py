
from json import dump
from automatonOmnijus import ConectCentral


central = ConectCentral(senha='omnijus01dev')
empresa = central.empresa('miojo')
processo = empresa.processo(4)
processo.registrar_tentativa_de_acao('colocar_agua_pra_ferver')
