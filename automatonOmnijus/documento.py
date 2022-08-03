
from attr import has
from automatonOmnijus.rotas import * 
from automatonOmnijus.requisicao import faz_requisicao
from automatonOmnijus.rotas import VISUALIZAR_DOCUMENTO
from requests import get,post
from json import loads


class Documento:

     def __init__(self,senha:str,ambiente:str,processo:str,nome:str=None,hash:str=None) -> None:
    
        self.num_processo = processo
        self.nome = nome
        self.hash = hash 
        self._senha = senha
        self._ambiente  = ambiente

     def cria_headers(self) -> None:
        return {
        'senha':self._senha,
        'ambiente':self._ambiente,
        'processo':str(self.num_processo),
        'documento':self.nome,
        'hash':self.hash,
        'baixar':'true'
       }

     def verifica_se_possui_headers_de_acesso(self):
        if not self.nome:
            raise ValueError('Nome do documento não definido')
        if not self.hash:
            raise ValueError('Hash do documento não definido')

     
     def baixar_binario_do_documento(self)->bytes:
         """ Baixa binário do documento
         Returns:
             bytes: o binário do documento 
         """ 
         self.verifica_se_possui_headers_de_acesso()
         req ={
            'url':f'{URL}{VISUALIZAR_DOCUMENTO}',
            'headers':self.cria_headers()
         }
         doc = get(**req)
         return doc.content
     
         
     def baixar_documento(self,path:str=None):
         """ Baixa o documento do processo
         Args:
             path (str, optional): Onde salvar o documento. Defaults to None.
         """
         if path is None:
            path = self.nome
         binario = self.baixar_binario_do_documento()
         with open(path,'wb') as f:
            f.write(binario)
            f.close() 
     

     def fazer_upload_de_documento(self,elemento:str or bytes):
         """Faz o upload do documento
         Args:
             elemento (str or bytes): O elemento a ser enviado podendo ser um path ou um binário
         """    
         if isinstance(elemento,str):
            if not self.nome:
                self.nome = elemento.split('/')[-1]

            with open(elemento,'rb') as f:
                binario = f.read()
         else:
            binario = elemento
         req ={
            'url':f'{URL}{ADICIONAR_DOCUMENTO_DO_PROCESSO}',
            'headers':self.cria_headers(),
            'data':binario
         }
         resp =  post(**req)
         if resp.status_code != 200:
            raise Exception(resp.text)

         dados = loads(resp.text)
         self.hash = dados['hash']
         
     def excluir(self):
         """Exclui o documento"""
         self.verifica_se_possui_headers_de_acesso()
         faz_requisicao(headers=self.cria_headers(),rota=EXCLUIR_DOCUMENTO_DO_PROCESSO)
    
        
     def gerar_url(self)->str:
         """_cria a url do Documento
         Returns:
             str: a url do documento 
         """
         query_string = ''
         copia_headers = self.cria_headers()
         copia_headers['baixar'] = 'false'
         copia_headers.pop('senha')
         for x in copia_headers:
             query_string += f'{x}={copia_headers[x]}&'
         return f'{URL}{VISUALIZAR_DOCUMENTO}?{query_string}'




     def __repr__(self):
        return f"""Documento: {self.nome}
Hash: {self.hash}
Query string: {self.gerar_url()}"""

