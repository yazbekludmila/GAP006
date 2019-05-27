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

    '''****** Exibe a msg "Em um campo numérico somente podem ser introduzidos numeros"""" ******'''
    context.inclui_parametro.abrir_criar_registro()
    context.inclui_parametro.digitar_cobertura('')
    context.inclui_parametro.digitar_modalidade('')
    context.app.escrever_direto('!@#$')
    context.app.digitos('tab')
    context.inclui_parametro.validar_mensagem(mensagem=r'data\images\msg_campo_numerico.PNG')
    context.inclui_parametro.fechar_criacao_de_registro()
    '''*****************************************************************************'''

    '''****** Exibe a msg "FORMATO NÃO VALIDO (ddMMyyyy)"."""" ******'''
    context.inclui_parametro.abrir_criar_registro()
    context.inclui_parametro.digitar_cobertura('')
    context.inclui_parametro.digitar_modalidade('')
    context.app.digitos('tab')
    context.inclui_parametro.preencher_vigencia('00000000', '')
    context.inclui_parametro.validar_mensagem(mensagem=r'data\images\msg_formato_nao_valido.PNG')
    context.inclui_parametro.fechar_criacao_de_registro()
    '''*****************************************************************************'''

    '''****** Exibe a msg "FORMATO NÃO VALIDO (ddMMyyyy)"."""" ******'''
    context.inclui_parametro.abrir_criar_registro()
    context.inclui_parametro.digitar_cobertura('')
    context.inclui_parametro.digitar_modalidade('')
    context.app.digitos('tab')
    context.inclui_parametro.preencher_vigencia(data_atual=context.tronweb.get_data_atual(), data_final='!@#!')
    context.inclui_parametro.validar_mensagem(mensagem=r'data\images\msg_campo_data.png')
    context.inclui_parametro.fechar_criacao_de_registro()
    '''*****************************************************************************'''

    '''****** Exibe a msg "FORMATO NÃO VALIDO (ddMMyyyy)"."""" ******'''
    context.inclui_parametro.abrir_criar_registro()
    context.inclui_parametro.digitar_cobertura('')
    context.inclui_parametro.digitar_modalidade('')
    context.app.digitos('tab')
    context.inclui_parametro.preencher_vigencia(data_atual=context.tronweb.get_data_atual(), data_final='00-00-0000')
    context.inclui_parametro.validar_mensagem(mensagem=r'data\images\msg_campo_data.png')
    context.inclui_parametro.fechar_criacao_de_registro()
    '''*****************************************************************************'''

    '''****** Exibe a msg "Em um campo numérico somente podem ser introduzidos numeros""""" ******'''
    context.inclui_parametro.abrir_criar_registro()
    context.inclui_parametro.digitar_cobertura('')
    context.inclui_parametro.digitar_modalidade('')
    context.app.digitos('tab')
    context.inclui_parametro.preencher_vigencia(data_atual=context.tronweb.get_data_atual(), data_final='!@#$')
    context.inclui_parametro.validar_mensagem(mensagem=r'data\images\msg_campo_data.png')
    context.inclui_parametro.fechar_criacao_de_registro()
    '''*****************************************************************************'''

    '''****** Exibe a msg "TAMANHO DO CAMPO INCORRETA"""""" ******'''
    context.inclui_parametro.abrir_criar_registro()
    context.inclui_parametro.digitar_cobertura('')
    context.inclui_parametro.digitar_modalidade('')
    context.app.digitos('tab')
    context.inclui_parametro.preencher_vigencia(data_atual=context.tronweb.get_data_atual(), data_final='2999')
    context.app.digitos('tab')
    context.inclui_parametro.validar_mensagem(mensagem=r'data\images\msg_tamanho_campo_incorreta.png')
    context.inclui_parametro.fechar_criacao_de_registro()
    '''*****************************************************************************'''

@then(u'incluo os parametros de resseguro invalidos apolice')
def step_impl(context):

    '''****** Exibe a msg "Em um campo numérico somente podem ser introduzidos numeros""""""" ******'''
    context.inclui_parametro.abrir_criar_registro()
    context.inclui_parametro.digitar_ramo('!@#$')
    context.inclui_parametro.validar_mensagem(mensagem=r'data\images\msg_campo_numerico.PNG')
    context.inclui_parametro.fechar_criacao_de_registro()
    '''*****************************************************************************'''
    
    '''****** Exibe a msg "VALOR INVALIDO"""""""" ******'''
    context.inclui_parametro.abrir_criar_registro()
    context.inclui_parametro.digitar_ramo('0')
    context.app.clica_imagem(r'data\images\aceitar3.PNG',similar=80)
    context.inclui_parametro.validar_mensagem(mensagem=r'data\images\msg_valor_invalido.PNG')
    context.inclui_parametro.fechar_criacao_de_registro()
    '''*****************************************************************************'''

    '''****** Exibe a msg "VALOR INVALIDO"""""""" ******'''
    context.inclui_parametro.abrir_criar_registro()
    context.inclui_parametro.digitar_ramo('18')
    context.app.escrever_direto('0')
    context.app.clica_imagem(r'data\images\aceitar3.PNG',similar=80)
    context.inclui_parametro.validar_mensagem(mensagem=r'data\images\msg_valor_invalido.PNG')
    context.inclui_parametro.fechar_criacao_de_registro()
    '''*****************************************************************************'''