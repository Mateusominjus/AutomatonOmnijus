from automatonOmnijus import ConectEmpresa


empresa = ConectEmpresa(senha='omnijus01dev',empresa='miojo')
r = empresa.acoes_pendentes()
print(r)