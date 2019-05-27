Feature: Enviar pagamento de sinistro

    Background: Login do Sistema
    Given que usuario esta logado sistema com usuario valido

    @CP067
    Scenario: Realizar abertura de sinistro de Endosso - Pagamento
    When abrir o Abertura de Sinistros
    And preencher os dados para abertura de sinistro de endosso - pagamento
    Then o sistema exibe tela com os expedientes do sinistro

    @CP068
    Scenario: Realizar abertura dos expedientes de sinistro de Endosso - Pagamentos
    When abrir o Abertura de Expedientes 
    And realizar busca pelo numero de sinistro de endosso - pagamento
    Then o sistema exibe tela com expdientes abertos

    @CP069
    Scenario: Realizar liquidação dos expedientes de sinistro de Endosso - Pagamentos
    When abrir o Liquidacao de Expedientes
    And realizar a busca pelo numero de sinistro de endosso - pagamento para Liquidacao
    Then a tela com os expedientes abertos e exibida com sucesso

    @CP072
    Scenario: Realizar abertura de sinistro de Apolice - Reservas
    When abrir o Abertura de Sinistros
    And preencher os dados para a abertura de sinistro de apolice - reservas
    Then o sistema exibe a tela com os expedientes do sinistro selecionado

    @CP075
    Scenario: Realizar abertura de sinistro de Endosso - Reservas
    When abrir o Abertura de Sinistros
    And preencher os dados para a abertura de sinistro de endosso - reservas
    Then o sistema exibe a tela com os expedientes do sinistro selecionado


