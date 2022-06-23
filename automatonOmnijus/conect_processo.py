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
        
