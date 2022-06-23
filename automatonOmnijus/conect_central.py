from automatonOmnijus.rotas import *
from automatonOmnijus.requisicao import faz_requisicao
from automatonOmnijus.conect_empresa import ConectEmpresa

class ConectCentral:

    def __init__(self,senha:str) -> None:
        self._senha = senha
        self._header = {
            'senha':senha
        }
        
    def empresa(self,empresa:str):
        return ConectEmpresa(senha=self._senha,empresa=empresa)


    def lista_logs_da_central(self):
        return faz_requisicao(header=self._header,rota=LOG_CENTRAL)

    def limpa_log_central(self):
        return faz_requisicao(header=self._header, rota=LIMPAR_LOG_CENTRAL)
    
