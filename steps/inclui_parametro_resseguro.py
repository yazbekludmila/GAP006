@then(u'incluo os parametros de reasseguro')
def step_impl(context):
    context.consulta_parametro.consulta_parametro_reasseguro('18', '117')
    # context.altera_parametro.altera_parametro()re21

@when(u'consulto parametros de resseguro')
def step_impl(context):
    raise NotImplementedError(u'STEP: When consulto parametros de resseguro')


@then(u'incluo os parametros de resseguro invalidos')
def step_impl(context):
    context.consulta_parametro.consulta_parametro_reasseguro('18', '117')
    
    