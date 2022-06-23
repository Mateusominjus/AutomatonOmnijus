

from automatonOmnijus.automaton_base import AutomatonBase


class Empresa(AutomatonBase):

    def __init__(self,senha:str,empresa:str) -> None:
        
       self._header = {
        'senha':senha,
        'empresa':empresa
       }


    def acoes_pendentes(self):
        pass 


    def todos_processos(self):
        pass 
    
    
