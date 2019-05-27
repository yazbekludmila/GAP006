Feature: Enviar Liquidacoes de Sinistro

    Background: Login do Sistema
    Given que usuario esta logado sistema com usuario valido

    @CP060
    Scenario: Realizar liquidacao dos expedientes de sinistro de Endosso - Liquidacoes
    When abrir o Liquidacao de Expedientes
    And realizar busca pelo numero do sinistro
    Then a tela de abertura de expedientes e exibida
    When realizar liquidacao dos expedientes
    Then a tela com expedientes abertos e exibida com sucesso

    @CP062
    Scenario: Realizar abertura de sinistro de apolice - Pagamento
    When abrir o Abertura de Sinistro
    And preencher os dados necessarios para a abertura de sinistro de apolice de Pagamento
    Then a tela exibindo os expedientes de sinistro de apolice de Pagamento

    @CP063
    Scenario: Realizar abertura dos expedientes de sinistro de Apolice - Pagamentos
    When abrir o Abertura de Sinistro
    And realizar busca por sinistro para abertura de expediente de apolice - pagamentos 
    Then a tela com os expedientes abertos e exibida com sucesso

    @CP064
    Scenario: Realizar liquidacao dos expedientes de sinistro de apolice - Pagamentos
    When abrir a Liquidacao de Expedientes
    And realizar busca por sinistro para realizar a liquidacao dos expedientes
    Then a tela com os expedientes abertos e exibidos

    @


