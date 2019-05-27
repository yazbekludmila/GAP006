Feature: Enviar sinistros fechados

   Background: Login do Sistema
   Given que usuario esta logado sistema com usuario valido

   @CP042
   Scenario: Realizar abertura de sinistro fechado de apolice
   When abrir o Abertura de Sinistros
   And preencher os campos necessarios para a abertura do sinistro de apolice durante sinistro fechado
   Then a abertura do sinistro de apolice nao sera realizada

   