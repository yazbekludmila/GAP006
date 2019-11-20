
@when(u'selecionar menu promotor')
def step_impl(context):
    context.gestoresapf.selecionar_menu_promotor()
    context.gestoresapf.selecionar_menu01()

@then(u'digitar TW INVALIDO CTS VALIDO e clicar BOTAO PESQUISAR')
def step_impl(context):
    context.gestoresapf.pesquisar_todos_promotores_cadastrados('TWTESTE','7905')

@then(u'digitar TW VALIDO CTS INVALIDO e clicar BOTAO PESQUISAR')
def step_impl(context):
    context.gestoresapf.pesquisar_todos_promotores_cadastrados('ALFCOSTA','9999')

@then(u'digitar TW BRANCO CTS ZERO e clicar BOTAO PESQUISAR')
def step_impl(context):
    context.gestoresapf.pesquisar_todos_promotores_cadastrados(' ','0')

@then(u'digitar TW VALIDO CTS VALIDO e clicar BOTAO PESQUISAR')
def step_impl(context):
    context.gestoresapf.pesquisar_todos_promotores_cadastrados('ALFCOSTA','7905')
   
@then(u'digitar TW INVALIDO CTS INVALIDO e clicar BOTAO PESQUISAR')
def step_impl(context):
    context.gestoresapf.pesquisar_todos_promotores_cadastrados('TWTESTE','9999')

@when(u'clicar x para fechar tela promotor')
def step_impl(context):
    context.gestoresapf.fechar_tela_promotores()

@then(u'tela promotores é fechada')
def step_impl(context):
    pass

@when(u'clicar x para fechar tela tw e clicar botao terminar')
def step_impl(context):
    context.gestoresapf.encerra_tw()

@then(u'tw é encerrado')
def step_impl(context):
    pass

