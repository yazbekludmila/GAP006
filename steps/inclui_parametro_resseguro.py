@then(u'incluo os parametros de reasseguro')
def step_impl(context):
    context.consulta_parametro.consulta_parametro_reasseguro('18', '117')
    # context.altera_parametro.altera_parametro()re21

@then(u'incluo os parametros de resseguro invalidos')
def step_impl(context):
    context.consulta_parametro.consulta_parametro_reasseguro('18', '117')
    