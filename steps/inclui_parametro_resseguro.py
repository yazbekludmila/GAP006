@when(u'consulto parametros de resseguro')
def step_impl(context):
    context.consulta_parametro.consulta_parametro_reasseguro('18', '117')

@then(u'incluo os parametros de reasseguro')
def step_impl(context):
    context.inclui_parametro.inclui_parametro_re21()

@then(u'incluo os parametros de resseguro invalidos enviar re21')
def step_impl(context):
    context.inclui_parametro.inclui_parametro_resseguro_invalido_re21()

@then(u'incluo os parametros de resseguro invalidos apolice')
def step_impl(context):
    context.inclui_parametro.inclui_parametro_resseguro_invalido_apolice()