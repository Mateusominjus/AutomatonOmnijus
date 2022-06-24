from copy import deepcopy
from automatonOmnijus.conect_processo import ConectProcesso
from automatonOmnijus.requisicao import faz_requisicao
from typing import List
from automatonOmnijus.rotas import *

class ConectEmpresa:

    def __init__(self,senha:str,empresa:str) -> None:
       
       self._senha = senha 
       self._empresa = empresa
       
       self._headers = {
        'senha':senha,
        'empresa':empresa
       }

    def processo(self,processo:int)->ConectProcesso:
        return ConectProcesso(senha=self._senha,empresa=self._empresa,processo=processo)
        
        
    def acoes_pendentes(self)->List[dict]:
        return faz_requisicao(headers=self._headers,rota=LISTAR_ACOES_PENDENTES)
    

    def todos_processos(self)->List[int]:
        return faz_requisicao(headers=self._headers,rota=TODOS_PROCESSOS)


    def estado_inicial(self)->dict:
        return faz_requisicao(headers=self._headers,rota=ESTADO_INICIAL)


    def modifica_estado_inicial(self,estado_inicial:dict)->str:
        return faz_requisicao(headers=self._headers,rota=MODIFICAR_ESTADO_INICIAL,body=estado_inicial)
    

    def modificar_acoes(self,acoes:dict):
        return faz_requisicao(headers=self._headers,rota=MODIFICAR_PROPRIEDADES_ACOES,body=acoes)
    

    def modificar_schema_do_processo(self,schema:dict):
        return faz_requisicao(headers=self._headers,rota=MODIFICAR_SCHEMA_DE_PROCESSO,body=schema)

    def modificar_arquivo_de_cerebro(self,arquivo_de_cerebro:str):
        novo_header = deepcopy(self._headers)
        novo_header['content-type'] = 'text/plain'
  
        return faz_requisicao(headers=novo_header,rota=MODIFICAR_ARQUIVO_DE_CEREBRO,body=arquivo_de_cerebro) 





    

