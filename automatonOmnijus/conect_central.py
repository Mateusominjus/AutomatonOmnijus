from automatonOmnijus.rotas import *
from automatonOmnijus.requisicao import faz_requisicao
from automatonOmnijus.conect_empresa import ConectEmpresa
from automatonOmnijus.conect_processo import ConectProcesso

class ConectCentral:

    def __init__(self,senha:str) -> None:
        self._senha = senha
        self._headers = {
            'senha':senha
        }
        
    def empresa(self,empresa:str)->ConectEmpresa:
        return ConectEmpresa(senha=self._senha,empresa=empresa)

    def processo(self,empresa:str,processo:int)->ConectProcesso:
        return ConectProcesso(senha=self._senha,empresa=empresa,processo=processo)
        
    
    
    def lista_logs_da_central(self):
        return faz_requisicao(headers=self._headers,rota=LOG_CENTRAL)

    def limpa_log_central(self):
        return faz_requisicao(headers=self._headers, rota=LIMPAR_LOG_CENTRAL)
    
