Feature: Enviar sinistros fechados

   Background: Login do Sistema
   Given que usuario esta logado sistema com usuario valido

   @CP042
   Scenario: Realizar abertura de sinistro fechado de apolice
   When abrir o Abertura de Sinistros
   And preencher os campos necessarios para a abertura do sinistro de apolice durante sinistro fechado
   Then a abertura do sinistro de apolice nao sera realizada

   
   @CP045
   Scenario: Realizar encerramento de sinistro de Endosso
   When abrir o Encerramento de Expedientes
   And preencher os campos necessarios para o encerramento do sinistro
   Then sinistro e encerrado com sucesso

   