from copy import deepcopy
from automatonOmnijus.requisicao import faz_requisicao
from typing import List
from automatonOmnijus.rotas import *



class ConexaoProcesso:

    def __init__(self,senha:str,ambiente:str,processo:str) -> None:
        self.num_processo = processo
        self._carregado = False 
        self._headers = {
        'senha':senha,
        'ambiente':ambiente,
        'processo':str(processo)
       }
    

    def verifica_se_esta_carregado(self):
        """Verifica se o processo está carregado"""
        if not self._carregado:
            raise Exception('O processo não foi carregado')


    def criar_processo(self,dados_do_processo:dict={},estado:dict={},acoes:List[dict]=[]):
        """Cria um novo processo novo
        Args:
            dados_do_processo (dict): Dicionário com os dados do processo
            estado (dict): Estado do processo
            acoes (List[dict]): Lista de ações do processo
        """
        novo_header = deepcopy(self._headers)
        novo_header['acao'] = 'criar'
        dados = {
            'processo':dados_do_processo,
            'estado':estado,
            'acoes':acoes
        }
        faz_requisicao(headers=novo_header,rota=CRIAR_PROCESSO,body=dados)
        self._carregado = True 



    def excluir_processo(self):
        """Exclui o processo"""    
        faz_requisicao(headers=self._headers,rota=EXCLUIR_PROCESSO)
        self._carregado = False
    
    def recriar_process(self,dados_do_processo:dict={},estado:dict={},acoes:List[dict]=[]):
        """Recria o processo
        Args:
            dados_do_processo (dict): Dicionário com os dados do processo
            estado (dict): Estado do processo
            acoes (List[dict]): Lista de ações do processo
        """
        self.excluir_processo()
        self.criar_processo(dados_do_processo,estado,acoes)
    


    def carregar_processo(self):
        """Carrega o processo
        Returns:
            dict: Dicionário com o processo
        """
        carregamento = faz_requisicao(headers=self._headers,rota=DADOS_DO_PROCESSO)
        self.dados_do_processo = carregamento['processo']
        self.estado = carregamento['estado']
        self.acoes = carregamento['acoes']
        self._carregado = True
    

    def salvar_processo(self):
        """Salva os dados do processo"""
        self.verifica_se_esta_carregado()
        novo_header = deepcopy(self._headers)    
        dados = {
            'processo':self.dados_do_processo,
            'estado':self.estado,
            'acoes':self.acoes
        }
        
        faz_requisicao(headers=self._headers,rota=MODIFICAR_PROCESSO,body=dados)


