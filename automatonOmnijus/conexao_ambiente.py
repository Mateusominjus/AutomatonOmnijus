from copy import deepcopy
from automatonOmnijus.conexao_processo import ConexaoProcesso
from automatonOmnijus.requisicao import faz_requisicao
from typing import List
from automatonOmnijus.rotas import *

class ConexaoAmbiente:

    def __init__(self,senha:str,ambiente:str) -> None:
        """ Construtor da classe Conexão Ambiente
        Args:
            senha (str): Senha da Central
            ambiente (str): Nome do ambiente
        """
        self._senha = senha
        self._ambiente = ambiente
        self._headers = {
            'senha':senha,
            'ambiente':ambiente
        }


    
    def excluir_todos_processos(self):
        """Exclui todos os processos da ambiente
        """
        return faz_requisicao(headers=self._headers,rota=REMOVER_TODOS_PROCESSOS)


    def acoes_em_erro(self)->dict:
        """Retorna um dicionário com as ações em erro
        Returns:
            dict: Dicionário com as ações em erro
        """
        return faz_requisicao(headers=self._headers,rota=ACOES_EM_ERRO)


    def adicionar_acao_em_erro(self,nome_da_acao:str,log:dict)->dict:
        """Adiciona uma ação em erro
        Args:
            nome_da_acao (str): Nome da ação
            log (dict): Log da ação
        Returns:
            dict: Dicionário com o log da ação
        """
        novo_header = deepcopy(self._headers)
        novo_header['acao'] = nome_da_acao
        return faz_requisicao(headers=novo_header,rota=ADICIONAR_ACAO_A_LISTA_DE_ERROS, body=log)
    
    
    def remover_acao_de_erro(self,nome_da_acao:str):
        """Remove uma ação de erro
        Args:
            nome_da_acao (str): Nome da ação
        """
        novo_header = deepcopy(self._headers)
        novo_header['acao'] = nome_da_acao
        return faz_requisicao(headers=novo_header,rota=REMOVER_ACAO_DA_LISTA_DE_ERROS)


    def numero_de_todos_processos(self)->List[int]:
        """Retorna uma lista com o número todos os processos da ambiente
        Returns:
            List[int]: Lista com os números de todos os processos
        """
        return faz_requisicao(headers=self._headers,rota=TODOS_PROCESSOS)





    

