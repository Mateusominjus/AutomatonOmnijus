
from attr import has
from automatonOmnijus.rotas import * 
from automatonOmnijus.requisicao import faz_requisicao
from automatonOmnijus.rotas import VISUALIZAR_DOCUMENTO
from requests import get,post
from json import loads


class DocumentoOffline:

     def __init__(self,nome:str) -> None:
        self.nome = nome
       
     
     def baixar_binario_do_documento(self)->bytes:
         """ Baixa binário do documento
         Returns:
             bytes: o binário do documento 
         """ 
         
     def baixar_documento(self,path:str=None):
         """ Baixa o documento do processo
         Args:
             path (str, optional): Onde salvar o documento. Defaults to None.
         """


     def fazer_upload_de_documento(self,elemento:str or bytes):
         """Faz o upload do documento
         Args:
             elemento (str or bytes): O elemento a ser enviado podendo ser um path ou um binário
         """    



     def __repr__(self):
        return f'Documento: {self.nome}'

