@EnviarApoliceParaRE21
Feature: Enviar Apolice e Endosso para RE21
   
   Background: Login do Sistema
   Given que usuario esta logado sistema com usuario valido

    @CP016
    Scenario: Realizar emissao de apolice manualmente com parametro para envio ao RE21
    When abrir o Emissao de Apolices e Endosso
    And preencher os campos necessarios da tela Emissao de Apolices Endossos
    And preencher os dados variaveis obrigatorios da Emissao de Apolices e Endossos
    Then a emissao de apolice e realizada com sucesso

    @CP017
    Scenario: Validar envio de Apolice ao RE21 conforme parametro
    When abrir o Cadastro Apolices Envio RE21
    And pesquisar pelo numero da apolice
    Then o sistema exibe tela com resultado da consulta da apolice

    @CP018
    Scenario: Realizar emissao de Endosso manualmente com parametro para envio ao RE21
    When abrir o Emissao de Apolices e Endosso
    And preencher os formularios necessarios para a emissao do endosso
    Then o endosso e emitido com sucesso

    @CP019
    Scenario: Validar envio de Endosso ao RE21 conforme parametro
    When abrir o Cadastro Apolices Envio RE21
    And pesquisar pelo numero do endosso
    Then o sistema exibe tela com resultado da consulta do endosso

    @CP020
    Scenario: Realizar emissao de Apolice manualmente sem parametro
    When abrir o Emissao de Apolices e Endosso
    And preencher os formularios necessarios para emissao de apolice sem parametro
    Then a apolice e gerada com sucesso

    @CP021
    Scenario: Validar o nao envio ao RE21 da Apolice sem parametro
    When abrir o Cadastro Apolices Envio RE21
    And pesquisar pelo numero da apolice gerada sem parametro
    Then o resultado da busca e exibida

    @CP022
    Scenario: Realizar emissao de endosso manualmente sem parametro
    When abrir o Emissao de Apolices e Endosso
    And preencher os dados para a emissao de endosso sem parametro
    Then a emissao e realizada com sucesso
    
    @CP023
    Scenario: Validar nao envio ao RE21 de Endosso sem parametro
    When abrir o Cadastro Apolices Envio RE21
    And preencher os dados com o endosso gerado sem parametro
    Then a validacao sobre o nao envio e exibida com sucesso

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

    







