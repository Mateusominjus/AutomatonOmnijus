from copy import deepcopy
from json import dumps,load,dump

from automatonOmnijus.documento_offline import DocumentoOffline


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
        if 'processo' in dados:
            self.dados_do_processo = dados['processo']
        if 'estado' in dados:
            self.estado = dados['estado']
        if 'acoes' in dados:
            self.acoes = dados['acoes']

        return self 




    def verifica_se_esta_carregado(self):
        """Verifica se o processo está carregado"""
        return True 


    def salvar_processo(self):
        """Salva os dados do processo
        Returns:         
            ConexaoProcesso: O próprio processo
        """
        return self 

    def salva_processo_em_json(self,path:str):
        """Salva o processo em um arquivo json
        Args:
            path (str): Caminho do arquivo
        """
        with open(path,'w') as f:
            dump(self.__dict__,f,indent=4)


    def novo_documento(self,nome:str=None):
        """Cria um novo documento
        Args:
            nome (str): Nome do documento
        Returns:
            Documento: Documento do processo
        """
        return DocumentoOffline(nome)



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
Estado: {self.estado}
Dados do processo: {dumps(self.dados_do_processo,indent=4)}
Acoes: {dumps(self.acoes,indent=4)}
"""
        return text