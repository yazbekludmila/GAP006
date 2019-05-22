@when(u'consulto parametros de reasseguro')
def step_impl(context):
    context.consulta_parametro.consulta_parametro_reasseguro('18','117')

@when(u'consulto parametros de reasseguro preenchendo somente ramo')
def step_impl(context):
    context.consulta_parametro.consulta_parametro_reasseguro('18','')

@then(u'mensagem de CAMPO OBRIGATORIO e exibido')
def step_impl(context):
    context.consulta_parametro.verifica_msg_campo_obrigatorio()  

@when(u'consulto parametros de reasseguro preenchendo somente produto')
def step_impl(context):
    context.consulta_parametro.consulta_parametro_reasseguro(ramo='',produto='117')

@when(u'consulto parametros de reasseguro sem preencher nenhum campo')
def step_impl(context):
    context.consulta_parametro.consulta_parametro_reasseguro('','')

@then(u'tela com os campos preenchidos da pesquisa e exibido')
def step_impl(context):
    pass