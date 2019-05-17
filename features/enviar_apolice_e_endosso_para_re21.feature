@EnviarApoliceParaRE21
Feature: Enviar Apolice e Endosso para RE21
   
   Background: 
   Given que usuario esta logado sistema com usuario valido

   @validar_envio_re21_endosso_parametro_inabilitado
    Scenario: Validar nao envio ao RE21 de Endosso como parametro inabilitado
    When clicar no botao Emissao
    And clicar no botao Menu de Atualizacoes
    And clicar no Cadastro Apolices Envio RE21
    Then a tela do Cadastro Apolices Envio RE21 e exibida
    When preencher numero da apolice ou endosso e clicar em consultar
    Then a pesquisa retorna informacoes sobre o numero informado

   @realizar_emissao_endosso_manual_parametro_inabilitado
    Scenario: Realizar emissao de endosso manual com parametro inabilitado
    When clicar no botao Emissao
    And clicar no botao Menu de Atualizacoes
    And clicar em Emissao de Apolices e Endossos
    Then a tela de Emissao de Apolices e Endossos e exibida com sucesso
    When preencher o campo PROD
    And preencher o campo Tipo de Emissao
    And preencher o campo Canal
    And preencher o campo Contrato


