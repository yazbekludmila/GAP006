@given(u'que usuario esta logado sistema com usuario valido')
def step_impl(context):
    print(context.dados.numero_de_cobertura())
    context.tronweb.validacao_tela(imagem=r"data\images\senha.png")
    context.tronweb.realizar_login()
    context.tronweb.validacao_tela(imagem=r'data\images\tron.PNG')