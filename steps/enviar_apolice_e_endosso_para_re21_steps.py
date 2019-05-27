
#****************** Cenário - Validar nao envio ao RE21 de Endosso como parametro inabilitado ***************#    

@when(u'preencher os dados para a consulta')
def step_impl(context):
    pass


@then(u'a pesquisa retorna informacoes sobre os dados informados')
def step_impl(context):
    pass

#******************** Cenário - Realizar emissao de endosso manual com parametro inabilitado ****************#

@when(u'preencher os formularios necessarios para a emissao do endosso')
def step_impl(context):
    context.tronweb.validacao_tela(imagem=r'data\images\campo_prod.png')

@when(u'aprova o Controle Tecnico')
def step_impl(context):
    pass


@then(u'a emissao do endosso e concluido com sucesso')
def step_impl(context):
    pass

#******************* Cenário - Realizar emissao de apolice manualmente com parametro para envio ao RE21 ***********#

@when(u'preencher os campos necessarios da tela Emissao de Apolices Endossos')
def step_impl(context):
    pass


@when(u'preencher os dados variaveis obrigatorios da Emissao de Apolices e Endossos')
def step_impl(context):
    pass