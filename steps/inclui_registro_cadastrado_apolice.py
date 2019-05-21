@then(u'incluo registros cadastrados na validacao da apolice')
def step_impl(context):
    context.inclui_parametro.inclui_registro_cadastrado_validacao_apolice()