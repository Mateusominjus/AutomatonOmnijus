from copy import deepcopy
from json import dumps,load


class ConexaoProcessoOffline:

    def __init__(self,processo:str) -> None:
        self.num_processo = processo
        self.dados_do_processo = {}
        self.estado = {}
        self.acoes = []
        
        
    def criar_processo(self):
        """Cria um novo processo novo
        Returns:         
           ConexaoProcesso: Novo processo
        """
        return self 
    


    def excluir_processo(self):
        """Exclui o processo
        Returns:         
            ConexaoProcesso: O processo existente
        """ 
        return  self 


    def carregar_processo(self):   
        """Carrega o processo
        Returns:
            ConexaoProcesso: O processo carregado
        """
        return self 
        
    def carregar_processo_via_json(self,path:str):
        """Carrega o processo
        Returns:
            ConexaoProcesso: O processo carregado
        """
        with open(path,'r') as f:
            dados = load(f)
        self.dados_do_processo = dados['processo']
        self.estado = dados['estado']
        self.acoes = dados['acoes']
        return self 




    def verifica_se_esta_carregado(self):
        """Verifica se o processo está carregado"""
        return True 


    def salvar_processo(self):
        """Salva os dados do processo
        Returns:         
            str: o texto retornado pela central
        """
  



    def novo_documento(self,nome:str=None):
        """Cria um novo documento
        Args:
            nome (str): Nome do documento
        Returns:
            Documento: Documento do processo
        """



    def documento(self,nome:str):
        """Retorna o documento com o nome passado
        Args:
            nome (str): Nome do documento
        Returns:
            Documento: Documento do processo
        """




    def __repr__(self) -> str:

        #ident the is of documents in tab 4

        text = '\n' + '=' *100 + f"""\nProcesso: {self.num_processo}
Carregado: {self._carregado}
Estado: {self.estado}
Dados do processo: {dumps(self.dados_do_processo,indent=4)}
Acoes: {dumps(self.acoes,indent=4)}
"""
        text+='Documentos:'
        for doc in self.documentos:
            text+='\n\t' + '-'* 100
            text += '\n\t' + str(doc).replace('\n','\n\t') 

        return text