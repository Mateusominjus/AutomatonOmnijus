from typing import Dict, List
from automatonOmnijus.rotas import *
from automatonOmnijus.requisicao import faz_requisicao
from automatonOmnijus.conect_ambiente import ConectAmbiente
from automatonOmnijus.conect_processo import ConectProcesso

class ConectCentral:

    def __init__(self,senha:str) -> None:
        self._senha = senha
        self._headers = {
            'senha':senha
        }
        
    def ambiente(self,empresa:str)->ConectAmbiente:
        """Retorna uma Conexão com o ambiente
        Args:
            empresa (str): Nome da empresa
        Returns:
            ConectEmpresa: Conexão com a empresa
        """

        return ConectAmbiente(senha=self._senha,empresa=empresa)

    def processo(self,empresa:str,processo:int)->ConectProcesso:

        return ConectProcesso(senha=self._senha,empresa=empresa,processo=processo)
        
    
    def lista_logs_da_central(self)->List[Dict]:
        """Retorna um dicionário com os logs da central
        Returns:
            dict: Dicionário com os logs da central 
        """
        return faz_requisicao(headers=self._headers,rota=LOG_CENTRAL)

    def limpa_log_central(self):
        """Limpa o log da central"""
        return faz_requisicao(headers=self._headers, rota=LIMPAR_LOG_CENTRAL)
    
