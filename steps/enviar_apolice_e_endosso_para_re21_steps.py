
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
    # Tela inicial emissão Apolices e Endossos #
    context.emissao.preencher_campo_prod(prod='117')
    context.emissao.preencher_tipo_de_emissao(emissao='R')
    context.emissao.preencher_canal(canal='99')
    context.emissao.preencher_contrato(contrato='99998')
    context.emissao.preencher_vigencia(vigencia='04062019')
    context.emissao.clicar_botao_prosseguir()
    # Segunda tela de emissão de Apolices #
    context.tronweb.validacao_tela(imagem=r'data\images\moeda.png')
    context.emissao.preencher_tomador(tomador='CGC',cnpj='3699845000105')
    context.emissao.preencher_corret(corret='24644')


@when(u'preencher os dados variaveis obrigatorios da Emissao de Apolices e Endossos')
def step_impl(context):
    pass