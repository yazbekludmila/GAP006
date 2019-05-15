@given(u'que usuario esta logado sistema com usuario valido')
def step_impl(context):
    context.login.realiza_login()
    context.login.valida_login()


@when(u'consulto parametros de reasseguro')
def step_impl(context):
    context.consulta_parametro.consulta_parametro_reasseguro()


@then(u'tela com os campos preenchidos da pesquisa e exibido')
def step_impl(context):
    context.consulta_parametro.consulta_parametro_reasseguro(ramo='',produto='')

@when(u'consulto parametros de reasseguro sem preencher nenhum campo')
def step_impl(context):
    context.consulta_parametro.consulta_parametro_reasseguro(ramo='',produto='')
