Feature: Incluir registro já cadastrado - Enviar RE21

   Background: Login no sistema
      Given que usuario esta logado sistema com usuario valido
   
   @inclui_registro_re21
   Scenario: Incluir  registro ja cadastrado enviar re21
      When consulto parametros de resseguro
      Then incluo registros cadastrados na opcao enviar re21