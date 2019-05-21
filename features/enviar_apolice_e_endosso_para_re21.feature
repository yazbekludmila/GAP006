@EnviarApoliceParaRE21
Feature: Enviar Apolice e Endosso para RE21
   
   Background: Login do Sistema
   Given que usuario esta logado sistema com usuario valido

    @validar_envio_re21_endosso_parametro_inabilitado
    Scenario: Validar nao envio ao RE21 de Endosso como parametro inabilitado
    When abrir o Cadastro Apolices Envio RE21
    And preencher os dados para a consulta
    Then a pesquisa retorna informacoes sobre os dados informados

    @realizar_emissao_de_endosso_manual_com_parametro_inabilitado
    Scenario: Realizar emissao de endosso manual com parametro inabilitado
    When abrir o Emissao de Apolices e Endosso
    And preencher os formularios necessarios para a emissao do endosso
    And aprova o Controle Tecnico
    Then a emissao do endosso e concluido com sucesso
    

    Scenario: Validar o nao envio ao RE21 de apolice com parametro inabilitado
    When clicar no botao Emissao
    And clicar no botao Menu de Atualizacoes
    And clicar no botao Cadastro Apolices Envio RE21
    Then a tela de Cadastro Apolices Envio RE21 e exibida com sucesso
    When realizar pesquisa pelo numero da apolice ou endosso
    Then o sistema exibe a tela com resultado da busca







