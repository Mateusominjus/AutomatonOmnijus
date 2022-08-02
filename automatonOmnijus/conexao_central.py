from typing import Dict, List
from automatonOmnijus.rotas import *
from automatonOmnijus.requisicao import faz_requisicao
from automatonOmnijus.conexao_ambiente import ConexaoAmbiente
from automatonOmnijus.conexao_processo import ConexaoProcesso

class ConexaoCentral:

    def __init__(self,senha:str) -> None:
        """Construtor da classe Conexão Central
        Args:
            senha (str): Senha da central
        """
        self._senha = senha
        self._headers = {
            'senha':senha
        }
        
    def ambiente(self,ambiente:str)->ConexaoAmbiente:
        """Retorna uma Conexão com o ambiente
        Args:
            ambiente (str): Nome do ambiente
        Returns:
            ConexaoAmbiente: Conexão com o ambiente
        """

        return ConexaoAmbiente(senha=self._senha,ambiente=ambiente)


    def processo(self,empresa:str,processo:int)->ConexaoProcesso:
        return ConexaoProcesso(senha=self._senha,empresa=empresa,processo=processo)
        
    
    def lista_logs_da_central(self)->List[Dict]:
        """Retorna um dicionário com os logs da central
        Returns:
            dict: Dicionário com os logs da central 
        """
        return faz_requisicao(headers=self._headers,rota=LOG_CENTRAL)

    def limpa_log_central(self):
        """Limpa o log da central"""
        return faz_requisicao(headers=self._headers, rota=LIMPAR_LOG_CENTRAL)
    
