Feature: Inclui parâmetro de reasseguro

   Background: Login no sistema
      Given que usuario esta logado sistema com usuario valido
   
   @inclui
   Scenario: Inclui parâmetro de reasseguro   
      When consulto parametros de reasseguro
      Then incluo os parametros de reasseguro
   
   @invalido_re21
   Scenario: Incluir parâmetros de resseguro invalidos enviar re21
      When consulto parametros de resseguro
      Then incluo os parametros de resseguro invalidos enviar re21

   @invalido_apolice
   Scenario: Incluir parâmetros de resseguro invalidos apolice
      When consulto parametros de resseguro
      Then incluo os parametros de resseguro invalidos apolice