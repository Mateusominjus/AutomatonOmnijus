from copy import deepcopy
from automatonOmnijus.requisicao import faz_requisicao
from typing import List
from automatonOmnijus.rotas import *

class ConectProcesso:

    def __init__(self,senha:str,empresa:str,processo:str) -> None:
        
        self._headers = {
        'senha':senha,
        'empresa':empresa,
        'processo':str(processo)
       }
    
    def dados_do_processo(self)->dict:
        return faz_requisicao(headers=self._headers,rota=DADOS_DO_PROCESSO)
        
    def completar_acao(self,nome_da_acao:str,informacoes_do_processo:dict=None,estado:dict=None):
        body = {}
        if informacoes_do_processo:
            body['informacoes_do_processo'] = informacoes_do_processo
        if estado:
            body['estado'] = estado
        
        novos_headers = deepcopy(self._headers)   
        novos_headers['acao'] = nome_da_acao


        return faz_requisicao(headers=novos_headers,rota=COMPLETAR_ACAO_PENDENTE,body=body)
     
     
    def registrar_tentativa_de_acao(self,nome_da_acao:str):
        pass 
