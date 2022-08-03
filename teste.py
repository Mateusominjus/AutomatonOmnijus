
from json import dump
from automatonOmnijus import ConexaoProcessoOffline

p1 = ConexaoProcessoOffline('12345')
p1.salvar_processo()
p1.carregar_processo_via_json('teste.json')
p1.salva_processo_em_json('saida.json')
print(p1)