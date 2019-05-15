Feature: Inclui parâmetro de reasseguro

   Background: Login no sistema
      Given que usuario esta logado sistema com usuario valido
   
   @inclui
   Scenario: Inclui parâmetro de reasseguro   
      When consulto parametros de reasseguro
      Then incluo os parametros de reasseguro

   Scenario: Incluir parâmetros de resseguro invalidos
      When consulto parametros de resseguro
      Then incluo os parametros de resseguro invalidos