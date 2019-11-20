#context.regrasapf          = PageConsultaRegrasApf(context.app)
#context.editaregrasapf     = PageEditarRegrasApf(context.app)

@when(u'alterar ALERTA INVALIDO E STATUS VALIDO') 
def step_impl(context):
    
    ''' Exibe a msg "SUPERADO TAMANHO REAL CAMPO  '''
    
    #context.editaregrasapf.digitar_alerta('111111111111111111111111111111111111111111111111111111111111111111111')
    #context.loginmenu.validacao_tela(imagem=r'data\images\erro_tamanho_regras.png')
    
    '''   Exibe a msg "CAMPO OBRIGATORIO '''

    context.editaregrasapf.digitar_alerta(' ')
    context.loginmenu.validacao_tela(imagem=r'data\images\erro_obrigatorio_regras.png')
    
    

@when(u'alterar ALERTA VALIDO E STATUS INVALIDO') 
def step_impl(context):
    
    ''' Exibe a msg "SUPERADO TAMANHO REAL CAMPO  '''
    
    #context.editaregrasapf.digitar_alerta('TESTE REGRAS ALERTA 00000000001')
    #context.editaregrasapf.digitar_status('AAAAA')
    #context.loginmenu.validacao_tela(imagem=r'data\images\erro_tamanho_regras.png')
    
    '''   Exibe a msg "CAMPO OBRIGATORIO '''

    context.editaregrasapf.digitar_alerta('TESTE REGRAS ALERTA 23 DE JULHOOOOOO')
    context.editaregrasapf.digitar_status(' ')
    context.loginmenu.validacao_tela(imagem=r'data\images\erro_obrigatorio_regras.png')
    
    
    '''  Exibe a msg "VALOR INVALIDO  '''  
    
    context.editaregrasapf.digitar_alerta('TESTE REGRAS ALERTA 23 DE JULHOOOOOO')
    context.editaregrasapf.digitar_status('@@')
    context.loginmenu.validacao_tela(imagem=r'data\images\erro_valor_invalido_regras.png')
    #context.editagestoresapf.fechar_janela_edicao

@when(u'alterar ALERTA E STATUS VALIDOS') 
def step_impl(context):
    context.editaregrasapf.digitar_alerta('TESTE ALTERACAO REGRAS ALERTA 23 DE JULHOOOOOO')
    context.editaregrasapf.digitar_status('A')
    context.loginmenu.validacao_tela(imagem=r'data\images\erro_vazia_regras.png')


@when(u'clicar botao NOVA ENTRADA e botao aceitar tela alerta')
def step_impl(context):
    context.editagestoresapf.efetiva_inclusao()  
    context.editaregrasapf.confirma_alteracoes_alerta()
    context.editaregrasapf.fechar_tela_alertas() 
    context.editaregrasapf.confirma_sair()

@then(u'exibir mensagem de erro e fechar janela edicao')
def step_impl(context):
     context.editagestoresapf.fechar_janela_edicao()

@when(u'clicar ACEITAR e X E SIM tela alertas')
def step_impl(context):
     context.editaregrasapf.confirma_alteracoes_alerta()
     context.editaregrasapf.fechar_tela_alertas() 
     context.editaregrasapf.confirma_sair() 

@when(u'clicar botao ACEITAR e botao aceitar tela alerta')
def step_impl(context):
     context.editagestoresapf.efetiva_alteracao()  
     context.editagestoresapf.confirma_alteracoes()
#     context.editagestoresapf.confirma_sair()

@when(u'clicar botao X e botao aceitar tela alerta')
def step_impl(context):
    context.editaregrasapf.excluir_regra()
    context.editagestoresapf.confirma_alteracoes() ### botao aceitar tela regras 

@then(u'alerta selecionado será excluído')
def step_impl(context):
    pass
    