Feature: Enviar ressarcimento de sinistro

   Background: Login do Sistema
   Given que usuario esta logado sistema com usuario valido

   @CP047
   Scenario: Realizar abertura de sinistro de Apólice - Ressarcimento
   When abrir o Parametrização de Envio Re21
   And preencher os campos necessarios para a abertura de sinistro de apolice - ressarcimento
   Then a tela para abertura dos expedientes e exibida com sucesso

   @CP048
   Scenario: Realizar abertura dos expedientes de sinistro de Apólice - Ressarcimento
   When abrir o Abertura de Expedientes
   And preencher os campos necessarios para a abertura dos expedientes
   Then a tela com expedientes abertos e exibida com sucesso

   @CP049
   Scenario: Realizar liquidação dos expedientes de sinistro de Apólice - Ressarcimento
   When abrir o Liquidação de Expedientes
   And realiza busca pelo numero do sinistro
   Then a tela de liquidacao com expedientes abertos e exibida com sucesso

   @CP051
   Scenario: Realizar abertura de sinistro de Endosso - Ressarcimento
   When abrir o Abertura de Sinistros
   And preencho os campos necessarios para abertura de sinistro de endosso - ressarcimento
   Then a tela com expedientes do sinistro e exibida

   @CP052
   Scenario: Realizar abertura dos expedientes de sinistro de Endosso - Ressarcimento
   When abrir o Abertura de Expedientes
   And realiza busca pelo numero do sinistro
   Then a tela com expedientes abertos e exibida


   @CP053
   Scenario: Realizar liquidação dos expedientes de sinistro de Endosso - Ressarcimento
   When abrir o Liquidação de Expedientes
   And realiza busca pelo numero do sinistro
   Then a tela com expedientes abertos liquidada e exibida

   #27
   @CP054
   Scenario: Validar envio de dados de ressarcimento de sinistros de Endosso ao RE21
   When 
   And 
   Then 

