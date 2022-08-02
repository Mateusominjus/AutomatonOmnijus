from typing import Dict, List
from automatonOmnijus.rotas import *
from automatonOmnijus.requisicao import faz_requisicao
from automatonOmnijus.conexao_ambiente import ConexaoAmbiente
from automatonOmnijus.conexao_processo import ConectProcesso

class ConexaoCentral:

    def __init__(self,senha:str) -> None:
        self._senha = senha
        self._headers = {
            'senha':senha
        }
        
    def ambiente(self,empresa:str)->ConexaoAmbiente:
        """Retorna uma Conexão com o ambiente
        Args:
            empresa (str): Nome da empresa
        Returns:
            ConectEmpresa: Conexão com a empresa
        """

        return ConexaoAmbiente(senha=self._senha,empresa=empresa)

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
    
