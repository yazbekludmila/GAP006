
############### CENÁRIO - Validar nao envio ao RE21 de Endosso como parametro inabilitado ####################

@when(u'abrir o {}')
def step_impl(context,opcao):
    context.tronweb.selecionar_menu_atualizacoes(opcao)


@when(u'preencher os dados para a consulta')
def step_impl(context):
    pass


@then(u'a pesquisa retorna informacoes sobre os dados informados')
def step_impl(context):
    pass