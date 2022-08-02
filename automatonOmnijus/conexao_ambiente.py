from copy import deepcopy
from automatonOmnijus.conexao_processo import ConexaoProcesso
from automatonOmnijus.requisicao import faz_requisicao
from typing import List
from automatonOmnijus.rotas import *

class ConexaoAmbiente:

    def __init__(self,senha:str,ambiente:str) -> None:
       self._senha = senha 
       self._ambiente = ambiente
       
       self._headers = {
        'senha':senha,
        'ambiente':ambiente
       }

    
    
    def excluir_todos_processos(self):
        """Exclui todos os processos da ambiente
        Returns:
            _type_: _description_
        """
        return faz_requisicao(headers=self._headers,rota=REMOVER_TODOS_PROCESSOS)


    def criar_processo(self,processo:str,body:dict={}):
        novo_header = deepcopy(self._headers)
        novo_header['processo'] = processo 
        return faz_requisicao(headers=novo_header,rota=CRIAR_PROCESSO,body=body)
         

    def acoes_em_erro(self)->dict:
        return faz_requisicao(headers=self._headers,rota=ACOES_EM_ERRO)


    def adicionar_acao_em_erro(self,nome_da_acao:str,log:dict)->dict:
        novo_header = deepcopy(self._headers)
        novo_header['acao'] = nome_da_acao
        return faz_requisicao(headers=novo_header,rota=ADICIONAR_ACAO_A_LISTA_DE_ERROS, body=log)
    
    
    def remover_acao_de_erro(self,nome_da_acao:str):
        novo_header = deepcopy(self._headers)
        novo_header['acao'] = nome_da_acao
        return faz_requisicao(headers=novo_header,rota=REMOVER_ACAO_DA_LISTA_DE_ERROS)


    def todos_processos(self)->List[int]:
        return faz_requisicao(headers=self._headers,rota=TODOS_PROCESSOS)





    

