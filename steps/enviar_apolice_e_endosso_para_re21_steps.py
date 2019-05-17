@when(u'clicar no botao Emissao')
def step_impl(context):
    context.menu.abrir_emissao()


@when(u'clicar no botao Menu de Atualizacoes')
def step_impl(context):
    context.menu.selecionar_menu_emissao('Menu de Atualizacoes')


@when(u'clicar no Cadastro Apolices Envio RE21')
def step_impl(context):
    context.menu.clicar_cadastro_apolice()


@then(u'a tela do Cadastro Apolices Envio RE21 e exibida')
def step_impl(context):
    context.menu.validar_tela_cadastro_apolices()


@when(u'preencher numero da apolice ou endosso e clicar em consultar')
def step_impl(context):
    context.menu.preencher_campo_apolice('111111')


@then(u'a pesquisa retorna informacoes sobre o numero informado')
def step_impl(context):
    pass

############################################################################################

@when(u'clicar em Emissao de Apolices e Endossos')
def step_impl(context):
    context.menu.selecionar_menu_emissao('Emissao Apolices Endossos')


@then(u'a tela de Emissao de Apolices e Endossos e exibida com sucesso')
def step_impl(context):
    context.menu.validar_tela_emissao_apolices()


@when(u'preencher o campo PROD')
def step_impl(context):
    context.menu.preencher_campo_prod()


@when(u'preencher o campo Tipo de Emissao')
def step_impl(context):
    context.menu.preencher_campo_tipo_de_emissao()


@when(u'preencher o campo Canal')
def step_impl(context):
    context.menu.preencher_campo_canal()


@when(u'preencher o campo Contrato')
def step_impl(context):
    pass