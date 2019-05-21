@then(u'incluo registros cadastrados na opcao enviar re21')
def step_impl(context):
    context.inclui_parametro.inclui_registro_cadastrado_enviar_re21()