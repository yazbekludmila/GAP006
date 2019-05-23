@when(u'consulto parametros de resseguro')
def step_impl(context):
    context.consulta_parametro.consulta_parametro_reasseguro('18', '117')

@then(u'incluo os parametros de reasseguro')
def step_impl(context):
    '''**************** Validação - Mensagem sucesso **********************'''
    context.inclui_parametro.abrir_criar_registro()
    context.inclui_parametro.digitar_cobertura(context.dados.cobertura())
    context.inclui_parametro.digitar_imp_segurada(context.dados.imp_segurada())
    context.inclui_parametro.preencher_vigencia(data_atual=context.tronweb.get_data_atual(),data_final=context.tronweb.get_data_futura())
    context.inclui_parametro.aceitar_criacao_registro()
    context.inclui_parametro.validar_mensagem(mensagem=r'data\images\vigencia_cadastrada.PNG')
    context.inclui_parametro.fechar_criacao_de_registro()
    '''********************************************************************'''
    
@then(u'incluo os parametros de resseguro invalidos enviar re21')
def step_impl(context):

    '''****** Exibe a msg "Em um campo numérico somente podem ser introduzidos numeros" ******'''
    context.inclui_parametro.abrir_criar_registro()
    context.inclui_parametro.digitar_cobertura('!@#$')
    context.inclui_parametro.validar_mensagem(mensagem=r'data\images\msg_campo_numerico.PNG')
    context.inclui_parametro.fechar_criacao_de_registro()
    '''*****************************************************************************'''

    '''****** Exibe a msg "VALOR INVALIDO"" ******'''
    context.inclui_parametro.abrir_criar_registro()
    context.inclui_parametro.digitar_ramo('0000')
    context.inclui_parametro.validar_mensagem(mensagem=r'data\images\msg_valor_invalido.PNG')
    context.inclui_parametro.fechar_criacao_de_registro()
    '''*****************************************************************************'''

    '''****** Exibe a msg "COBERTURA INVALIDA PARA O PRODUTO""" ******'''
    context.inclui_parametro.abrir_criar_registro()
    context.inclui_parametro.digitar_cobertura('0')
    context.inclui_parametro.validar_mensagem(mensagem=r'data\images\msg_cobertura_invalida.PNG')
    context.inclui_parametro.fechar_criacao_de_registro()
    '''*****************************************************************************'''

    '''****** Exibe a msg "Em um campo numérico somente podem ser introduzidos numeros"""" ******'''
    context.inclui_parametro.abrir_criar_registro()
    context.inclui_parametro.digitar_cobertura('9999')
    context.inclui_parametro.digitar_modalidade('!@#$')
    context.inclui_parametro.validar_mensagem(mensagem=r'data\images\msg_campo_numerico.PNG')
    context.inclui_parametro.fechar_criacao_de_registro()
    '''*****************************************************************************'''

@then(u'incluo os parametros de resseguro invalidos apolice')
def step_impl(context):
    context.inclui_parametro.inclui_parametro_resseguro_invalido_apolice()