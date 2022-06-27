
from json import dump
from automatonOmnijus import ConectCentral


central = ConectCentral(senha='omnijus01dev')
empresa = central.empresa('miojo')
processo = empresa.processo(6)
processo.completar_acao('colocar_agua_pra_ferver',informacoes_do_processo={'aa':222})