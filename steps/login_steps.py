@given(u'que usuario esta logado sistema com usuario valido')
def step_impl(context):
    context.tronweb.realizar_login()
    context.tronweb.validacao_tela(imagem=r'data\images\tron.PNG')