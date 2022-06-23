from automatonOmnijus.rotas import *
from json import JSONDecodeError,loads
from requests import get


class AutomatonBase:

    def __init__(self,senha:str) -> None:
        self._senha = senha
        self._header = {
            'senha':senha
        }
    
    def _faz_requisicao(self,rota,body=None)->str or dict or list:


        if rota not in ROTAS_VALIDAS:
            raise Exception(f'a rota "{rota}" não existe')
            
        URL = 'https://75s7k5xf4ebqh2sofe676zh7gm0vedtt.lambda-url.us-east-1.on.aws'
        req ={
         'url':f'{URL}{rota}',
         'headers':self._header
        }
        if body.__class__ == dict:
            req['json']= body

        http = get(**req)

        if http.status_code != 200:
            raise Exception(http.text)
        
        else:
            try:
                return loads(http.text)
            except JSONDecodeError:
                return http.text
        

