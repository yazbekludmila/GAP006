@when(u'consulto parametros de resseguro')
def step_impl(context):
    context.consulta_parametro.consulta_parametro_reasseguro('18', '117')

@then(u'incluo os parametros de reasseguro')
def step_impl(context):
    context.inclui_parametro.inclui_parametro()

@then(u'incluo os parametros de resseguro invalidos')
def step_impl(context):
    context.inclui_parametro.inclui_parametro_resseguro_invalido()