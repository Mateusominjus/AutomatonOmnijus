from automatonOmnijus.rotas import *
from automatonOmnijus.automaton_base import AutomatonBase
from automatonOmnijus.empresa import Empresa

class AutomatonOmnijus(AutomatonBase):

    def empresa(self,empresa:str):
        return Empresa(self._senha,empresa)

    def lista_logs_da_central(self):
        return self._faz_requisicao(LOG_CENTRAL)

    def limpa_log_central(self):
        return self._faz_requisicao(LIMPAR_LOG_CENTRAL)
    
