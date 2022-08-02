
from json import dump
from automatonOmnijus import ConectCentral


central = ConectCentral(senha='omnijus01dev')
r = central.limpa_log_central()
print(r)
