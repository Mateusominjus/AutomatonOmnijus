from automatonOmnijus.requisicao import faz_requisicao
from typing import List
from automatonOmnijus.rotas import *

class ConectEmpresa:

    def __init__(self,senha:str,empresa:str) -> None:
        
       self._header = {
        'senha':senha,
        'empresa':empresa
       }


    def acoes_pendentes(self)->List[dict]:
        return faz_requisicao(header=self._header,rota=LISTAR_ACOES_PENDENTES)
    

    def todos_processos(self)->List[int]:
        return faz_requisicao(header=self._header,rota=TODOS_PROCESSOS)




    

