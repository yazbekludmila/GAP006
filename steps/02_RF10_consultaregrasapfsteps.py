
#context.regrasapf          = PageConsultaRegrasApf(context.app)
#context.editaregrasapf     = PageEditarRegrasApf(context.app)

@when(u'selecionar menu regras de alerta')
def step_impl(context):
    context.regrasapf.selecionar_menu_regras_Alerta()
    context.regrasapf.selecionar_menu_regras_Alerta02()

@then(u'digitar ID ZERO STATUS BRANCO e clicar BOTAO PESQUISAR')
def step_impl(context):
    context.regrasapf.pesquisar_todos_alertas_cadastrados('0',' ')

@then(u'digitar ID INVALIDO STATUS VALIDO e clicar BOTAO PESQUISAR')
def step_impl(context):
    context.regrasapf.pesquisar_todos_alertas_cadastrados('20','A')

@then(u'digitar ID VALIDO STATUS INVALIDO e clicar BOTAO PESQUISAR')
def step_impl(context):
    context.regrasapf.pesquisar_todos_alertas_cadastrados('14','B')

@then(u'digitar ID VALIDO STATUS VALIDO e clicar BOTAO PESQUISAR')
def step_impl(context):
    context.regrasapf.pesquisar_todos_alertas_cadastrados('202','A')

@when(u'clicar x para fechar tela REGRAS ALERTA')
def step_impl(context):
    context.regrasapf.fechar_tela_alertas()

@then(u'tela alertas é fechada')
def step_impl(context):
    pass


