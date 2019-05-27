Feature: Enviar Sinistros Abertos

   Background: Login do Sistema
   Given que usuario esta logado sistema com usuario valido

   @CP036
   Scenario: Realizar abertura de sinistro de apolice
   When abrir o Abertura de Sinistros
   And preencher os campos necessarios para a abertura dos sinistros de apolice
   Then a tela com os expedientes do sinistro de apolice e exibida com sucesso

   @CP037
   Scenario: Realizar abertura dos expedientes de sinistro de apolice
   When abrir o Abertura de Expedientes 
   And realizar a busca pelo numero do sinistro de apolice
   And realizar abertura dos expedientes de apolice
   Then a tela de expedientes abertos de apolice e exibido com sucesso

   @CP039
   Scenario: Realizar abertura de sinistro de Endosso
   When abrir o Abertura de Sinistros
   And preencher os campos necessarios para a abertura dos sinistros
   Then a tela com os expedientes do sinistro de endosso e exibida com sucesso

   @CP040
   Scenario: Realizar abertura dos expedientes de sinistro de endosso
   When abrir o Abertura de Expedientes
   And realizar a busca pelo numero do sinistro de endosso
   And realizar abertura dos expedientes de endosso
   Then a tela de expedientes abertos de endosso e exibido com sucesso



