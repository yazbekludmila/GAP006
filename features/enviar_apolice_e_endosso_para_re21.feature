@EnviarApoliceParaRE21
Feature: Enviar Apolice e Endosso para RE21
   
   Background: Login do Sistema
   Given que usuario esta logado sistema com usuario valido

    @CP016
    Scenario: Realizar emissao de aplice manualmente com parametro para envio ao RE21
    When abrir o Emissao de Apolices e Endosso
    And preencher os campos necessarios da tela Emissao de Apolices Endossos
    And preencher os dados variaveis obrigatorios da Emissao de Apolices e Endossos

    @CP031
    Scenario: Validar o nao envio ao RE21 de endosso com data de emissao superior a parametrizada
    When abrir o Cadastro Apolices Envio RE21
    And realizar busca do endosso com data de emissao superior a parametrizada
    Then a mensagem de erro e exibida com sucesso

    @CP032
    Scenario: Realizar emissão de Apolice manual com parametro inabilitado
    When abrir o Emissao de Apolices e Endosso
    And preencher os formularios para a emissao da apolice
    And realizar a aprovacao do controle Tecnico
    Then a emissao e realizada com sucesso

    @CP033
    Scenario: Validar o nao envio ao RE21 de apolice com parametro inabilitado
    When abrir o Cadastro Apolices Envio RE21
    And preencher os dados para o envio de apolice
    Then a pesquisa retorna informacoes sobre os dados informados

    @CP034
    Scenario: Realizar emissao de endosso manual com parametro inabilitado
    When abrir o Emissao de Apolices e Endosso
    And preencher os formularios necessarios para a emissao do endosso
    And aprova o Controle Tecnico
    Then a emissao do endosso e concluido com sucesso
    
    @CP035
    Scenario: Validar nao envio ao RE21 de endosso como parametro inabilitado
    When abrir o Cadastro Apolices Envio RE21
    And preencher os dados para o envio de endosso
    Then a pesquisa retorna informacoes sobre os dados informados

    







