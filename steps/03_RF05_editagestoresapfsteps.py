@when(u'clicar botao lapis')
def step_impl(context):
    context.editagestoresapf.habilitar_edicao()
     

@then(u'exibida tela para edicao dos dados')
def step_impl(context):
    pass


@when(u'alterar usuario tw  tipo  e ativo validos')
def step_impl(context):
     context.editagestoresapf.digitar_usertw('ALFCOSTA')
     context.editagestoresapf.digitar_tipo('PROMOTOR')
     context.editagestoresapf.digitar_ativo('NAO')
     context.loginmenu.validacao_tela(imagem=r'data\images\msgerro_vazia_alteracao.png') 
         
@when(u'alterar USUARIO TW INVALIDO e tipo e ativo validos')
def step_impl(context):
    #    '''****** Exibe a msg "USUARIO TW NAO ENCONTRADO ##  
    
    context.editagestoresapf.digitar_usertw('CINHE')
    context.loginmenu.validacao_tela(imagem=r'data\images\erro_tw_nao_cadastr.png')
    
#    '''****** Exibe a msg "SUPERSDO TAMANHO EREEAL CAMPO  ##  
     
    context.editagestoresapf.digitar_usertw('CNHEIRRRRRR')
    context.loginmenu.validacao_tela(imagem=r'data\images\erro_tamanho.png')
    
#    '''****** Exibe a msg "CAMPO OBRIGATORIO ##  
    ##context.editagestoresapf.habilitar_edicao()
    context.editagestoresapf.digitar_usertw('         ')
    context.loginmenu.validacao_tela(imagem=r'data\images\erro_obrigatorio.png')
    
    ##context.editagestoresapf.fechar_alteracao_promotor
#    '''****** Exibe a msg "VALOR INVALIDO##  
    ##context.editagestoresapf.habilitar_edicao()
    context.editagestoresapf.digitar_usertw('####@@@@#')
    context.loginmenu.validacao_tela(imagem=r'data\images\erro_tw_invalido.png')
    context.editagestoresapf.fechar_janela_edicao
 
@when(u'alterar TIPO INVALIDO E USUARIO E ATIVO validos')
def step_impl(context):
    #    '''****** Exibe a msg "tipo NAO ENCONTRADO ##  
    
    context.editagestoresapf.digitar_usertw('ALFCOSTA')
    context.editagestoresapf.digitar_tipo('coord')
    context.loginmenu.validacao_tela(imagem=r'data\images\erro_tipo_invalido.png')
     
#    '''****** Exibe a msg "SUPERSDO TAMANHO EREEAL CAMPO  ##  
    ##context.editagestoresapf.habilitar_edicao()
    #context.editagestoresapf.digitar_usertw('ALFCOSTA')
    context.editagestoresapf.digitar_tipo('coordenad')
    context.loginmenu.validacao_tela(imagem=r'data\images\erro_tamanho.png')
        
#    '''****** Exibe a msg "CAMPO OBRIGATORIO ##  
    ##context.editagestoresapf.habilitar_edicao()
    #context.editagestoresapf.digitar_usertw('ALFCOSTA')
    context.editagestoresapf.digitar_tipo('         ')
    context.loginmenu.validacao_tela(imagem=r'data\images\erro_obrigatorio.png')
     
    ##context.editagestoresapf.fechar_alteracao_promotor
#    '''****** Exibe a msg "VALOR INVALIDO##  
    ##context.editagestoresapf.habilitar_edicao()
    #context.editagestoresapf.digitar_usertw('ALFCOSTA')
    context.editagestoresapf.digitar_tipo('####@@@@#')
    context.loginmenu.validacao_tela(imagem=r'data\images\erro_tipo_invalido.png')
    context.editagestoresapf.fechar_janela_edicao

@when(u'alterar ATIVO INVALIDO E USUARIO E TIPO validos')
def step_impl(context):
    #    '''******  Exibe a msg "ativo NAO ENCONTRADO ##  
    
    context.editagestoresapf.digitar_usertw('ALFCOSTA')
    context.editagestoresapf.digitar_tipo('PROMOTOR')
    context.editagestoresapf.digitar_ativo('TAL')
    context.loginmenu.validacao_tela(imagem=r'data\images\erro_ativo_invalido.png')
    ##context.editagestoresapf.fechar_janela_edicao

#    '''****** Exibe a msg "SUPERSDO TAMANHO EREEAL CAMPO  ##  
    #context.editagestoresapf.digitar_usertw('ALFCOSTA')
    #context.editagestoresapf.digitar_tipo('PROMOTOR')
    context.editagestoresapf.digitar_ativo('mmmmm')
    context.loginmenu.validacao_tela(imagem=r'data\images\erro_tamanho.png')
    
    
#    '''****** Exibe a msg "CAMPO OBRIGATORIO ##  
    #context.editagestoresapf.digitar_usertw('ALFCOSTA')
    #context.editagestoresapf.digitar_tipo('PROMOTOR')
    context.editagestoresapf.digitar_ativo('   ')
    context.loginmenu.validacao_tela(imagem=r'data\images\erro_obrigatorio.png')
    
#    '''****** Exibe a msg "VALOR INVALIDO##  
    #context.editagestoresapf.digitar_usertw('ALFCOSTA')
    #context.editagestoresapf.digitar_tipo('PROMOTOR')
    context.editagestoresapf.digitar_ativo('@@#')
    context.loginmenu.validacao_tela(imagem=r'data\images\erro_ativo_invalido.png')
    context.editagestoresapf.fechar_janela_edicao

@then(u'exibir mensagem de erro')
def step_impl(context):
    pass

@when(u'clicar botao Aceitar e botao aceitar tela promotores')
def step_impl(context):
    #botao aceitar janela edicao
    context.editagestoresapf.efetiva_alteracao()  
    context.editagestoresapf.confirma_alteracoes() ## botao aceitar tela promotores"

@when(u'clicar botao +')
def step_impl(context):
    context.editagestoresapf.habilitar_inclusao()

@when(u'clicar botao NOVA ENTRADA e botao aceitar tela promotores')
def step_impl(context):
    context.editagestoresapf.efetiva_inclusao()  
    context.editagestoresapf.confirma_alteracoes() ## botao aceitar tela promotores"
    

