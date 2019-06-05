import time

@given(u'que usuario esta logado sistema com usuario valido')
def step_impl(context):
    time.sleep(6)
    context.tronweb.validacao_tela(imagem=r'data\images\usuario_inexistente.png')
    context.tronweb.realizar_login()
    context.tronweb.validacao_tela(imagem=r'data\images\tron.PNG')

@when(u'abrir o {}')
def step_impl(context,opcao):
    context.tronweb.selecionar_menu_atualizacoes(opcao)
    