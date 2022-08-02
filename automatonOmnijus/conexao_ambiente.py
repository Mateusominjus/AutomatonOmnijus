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

    def processo(self,processo:int,carregar:bool=False)->ConexaoProcesso:
        """Retorna uma Conexão com o processo
        Args:
            processo (int): Número do processo
        Returns:
            ConexaoProcesso: Conexão com o processo
        """
        return ConexaoProcesso(senha=self._senha,ambiente=self._ambiente,processo=processo,carregar=carregar)
    




    def excluir_todos_processos(self):
        """Exclui todos os processos da ambiente
        Returns:         
            str: o texto retornado pela central
        """
        return faz_requisicao(headers=self._headers,rota=REMOVER_TODOS_PROCESSOS)


    def acoes_em_erro(self)->dict:
        """Retorna um dicionário com as ações em erro
        Returns:
            dict: Dicionário com as ações em erro
        """
        return faz_requisicao(headers=self._headers,rota=ACOES_EM_ERRO)


    def adicionar_acao_em_erro(self,nome_da_acao:str,log:dict):
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
        Returns:         
            str: o texto retornado pela central
        """
        novo_header = deepcopy(self._headers)
        novo_header['acao'] = nome_da_acao
        return faz_requisicao(headers=novo_header,rota=REMOVER_ACAO_DA_LISTA_DE_ERROS)


    def remover_todas_acoes_da_lista_de_erros(self):
        """Remove todas as ações da lista de erros
        Returns:         
            str: o texto retornado pela central
        """
        return faz_requisicao(headers=self._headers,rota=REMOVER_TODAS_ACOES_DA_LISTA_DE_ERROS)
    

    def numero_de_todos_processos(self)->List[int]:
        """Retorna uma lista com o número todos os processos da ambiente
        Returns:
            List[int]: Lista com os números de todos os processos
        """
        return faz_requisicao(headers=self._headers,rota=TODOS_PROCESSOS)

    def processos(self)->List[ConexaoProcesso]:
        """Retorna uma lista com todos os processos da ambiente
        Returns:
            List[ConexaoProcesso]: Lista com todos os processos
        """
        return [self.processo(processo) for processo in self.numero_de_todos_processos()]



    

