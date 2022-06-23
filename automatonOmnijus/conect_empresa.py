from automatonOmnijus.conect_processo import ConectProcesso
from automatonOmnijus.requisicao import faz_requisicao
from typing import List
from automatonOmnijus.rotas import *

class ConectEmpresa:

    def __init__(self,senha:str,empresa:str) -> None:
       
       self._senha = senha 
       self._empresa = empresa
       
       self._header = {
        'senha':senha,
        'empresa':empresa
       }

    def processo(self,empresa:str,processo:int)->ConectProcesso:
        return ConectProcesso(senha=self._senha,empresa=empresa,processo=processo)
        
        
    def acoes_pendentes(self)->List[dict]:
        return faz_requisicao(header=self._header,rota=LISTAR_ACOES_PENDENTES)
    

    def todos_processos(self)->List[int]:
        return faz_requisicao(header=self._header,rota=TODOS_PROCESSOS)


    def estado_inicial(self)->dict:
        return faz_requisicao(header=self._header,rota=ESTADO_INICIAL)


    def modifica_estado_inicial(self,estado_inicial:dict)->str:
        return faz_requisicao(header=self._header,rota=MODIFICAR_ESTADO_INICIAL,body=estado_inicial)
    




    

