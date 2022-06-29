# rotas globais
LOG_CENTRAL = '/dev/log_central'
LIMPAR_LOG_CENTRAL ='/dev/limpar_log_central'
CRIAR_EMPRESA = '/dev/criar_empresa'
LISTAR_EMPRESAS = '/dev/listar_empresas'


#rotas de empresa
ESTADO_INICIAL = '/dev/estado_inicial'
MODIFICAR_ESTADO_INICIAL =  '/dev/modificar_estado_inicial'
SCHEMA_DE_PROCESSO = '/dev/schema_de_processo'
ACOES_EM_ERRO = '/acoes_em_erro'
ADICIONAR_ACAO_A_LISTA_DE_ERROS = '/adicionar_acao_a_lista_de_erros'
REMOVER_ACAO_DA_LISTA_DE_ERROS ='/remover_acao_da_lista_de_erros'
MODIFICAR_SCHEMA_DE_PROCESSO = '/dev/modificar_schema_de_processo'
PROPRIEDADES_DE_ACOES = '/dev/propriedades_de_acoes'
MODIFICAR_PROPRIEDADES_ACOES =  '/dev/modificar_propriedades_acoes'
ARQUIVO_DE_CEREBRO = '/dev/arquivo_de_cerebro'
MODIFICAR_ARQUIVO_DE_CEREBRO = '/dev/modificar_cerebro'
TODOS_PROCESSOS =  '/todos_processos'
LISTAR_ACOES_PENDENTES ='/acoes_pendentes'
REMAPEAR_TODOS_PROCESSOS ='/dev/remapear_todos_processos'
EXCLUIR_TODOS_PROCESSOS = '/dev/excluir_todos_processos'
#rotas de processo 
DADOS_DO_PROCESSO = '/dados_do_processo'
MODIFICAR_PROCESSO = '/modificar_processo'
CRIAR_PROCESSO = '/criar_processo'
COMPLETAR_ACAO_PENDENTE = '/completar_acao'
REGISTRAR_TENTATIVA_DE_ACAO_PENDENTE =  '/registrar_tentativa_de_acao'
EXCLUIR_PROCESSO = '/dev/excluir_processo'
LOGS_DO_PROCESSO =  '/logs_do_processo'
ROTAS_VALIDAS = [
    LOG_CENTRAL,
    LIMPAR_LOG_CENTRAL,
    LISTAR_EMPRESAS,
    ESTADO_INICIAL,
    MODIFICAR_ESTADO_INICIAL,
    EXCLUIR_TODOS_PROCESSOS,
    SCHEMA_DE_PROCESSO,
    ACOES_EM_ERRO,
    ADICIONAR_ACAO_A_LISTA_DE_ERROS,
    REMOVER_ACAO_DA_LISTA_DE_ERROS,
    MODIFICAR_SCHEMA_DE_PROCESSO,
    PROPRIEDADES_DE_ACOES,
    MODIFICAR_PROPRIEDADES_ACOES,
    LOGS_DO_PROCESSO,
    ARQUIVO_DE_CEREBRO,
    MODIFICAR_ARQUIVO_DE_CEREBRO,
    LISTAR_ACOES_PENDENTES,
    TODOS_PROCESSOS,
    REMAPEAR_TODOS_PROCESSOS,
   DADOS_DO_PROCESSO,
   MODIFICAR_PROCESSO,
   COMPLETAR_ACAO_PENDENTE,
   REGISTRAR_TENTATIVA_DE_ACAO_PENDENTE,
   EXCLUIR_PROCESSO,
   CRIAR_PROCESSO
]




