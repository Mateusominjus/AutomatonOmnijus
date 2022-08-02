
from automatonOmnijus.rotas import * 
import base64
from automatonOmnijus.requisicao import faz_requisicao
from automatonOmnijus.rotas import VISUALIZAR_DOCUMENTO
from requests import get

class Documento:

     def __init__(self,senha:str,ambiente:str,nome:str,hash:str,processo:str,offline:bool=False) -> None:
        self.num_processo = processo
        self.nome = nome
        self.hash = hash
        self._offline = offline 
        
        self._headers = {
        'senha':senha,
        'ambiente':ambiente,
        'processo':str(processo),
        'documento':nome,
        'hash':hash,
        'baixar':'true'
       }
    
    
     def baixar_binario_do_documento(self):
        req ={
            'url':f'{URL}{VISUALIZAR_DOCUMENTO}',
            'headers':self._headers
        }
        doc = get(**req)
        return doc.content

    
     def salvar(self,local:str):
        pass 

