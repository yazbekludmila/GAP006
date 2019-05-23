@CadastrarParametro
Feature: Cadastrar parâmetros de resseguro para integração com sistema RE21

   Background: Login no sistema
      Given que usuario esta logado sistema com usuario valido
   
   @CP001
   Scenario: Consultar parâmetro de reasseguro   
      When abrir o Parametrizacao do Envio Re21
      And consulto parametros de reasseguro
      Then tela com os campos preenchidos da pesquisa e exibido

   @CP002
   Scenario: Consultar parâmetro de reasseguro preenchendo somente ramo
      When abrir o Parametrizacao do Envio Re21
      And consulto parametros de reasseguro preenchendo somente ramo
      Then mensagem de CAMPO OBRIGATORIO e exibido

   @CP003
   Scenario: Consultar parâmetro de reasseguro preenchendo somente produto
      When abrir o Parametrizacao do Envio Re21
      And consulto parametros de reasseguro preenchendo somente produto
      Then mensagem de CAMPO OBRIGATORIO e exibido

   @CP004
   Scenario: Consultar parâmetro de reasseguro sem preencher nenhum campo
      When abrir o Parametrizacao do Envio Re21
      And consulto parametros de reasseguro sem preencher nenhum campo
      Then mensagem de CAMPO OBRIGATORIO e exibido

   @CP009
   Scenario: Inclui parâmetro de reasseguro
      When abrir o Parametrizacao do Envio Re21
      And consulto parametros de reasseguro
      Then incluo os parametros de reasseguro

   @CP010
   Scenario: Incluir parâmetros de resseguro invalidos enviar re21
      When abrir o Parametrizacao do Envio Re21
       And consulto parametros de resseguro
      Then incluo os parametros de resseguro invalidos enviar re21

   @CP011
   Scenario: Incluir parâmetros de resseguro invalidos apolice
      When abrir o Parametrizacao do Envio Re21
      And consulto parametros de resseguro
      Then incluo os parametros de resseguro invalidos apolice

   @CP014
   Scenario: Incluir registro ja cadastrados validacao apolice
      When abrir o Parametrizacao do Envio Re21
      And consulto parametros de resseguro
      Then incluo registros cadastrados na validacao da apolice
      
   @CP015
   Scenario: Incluir  registro ja cadastrado enviar re21
      When abrir o Parametrizacao do Envio Re21
      And consulto parametros de resseguro
      Then incluo registros cadastrados na opcao enviar re21