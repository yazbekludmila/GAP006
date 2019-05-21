Feature: Incluir registro já cadastrado - Validação Apolice

   Background: Login no sistema
      Given que usuario esta logado sistema com usuario valido
   
   @inclui_registro_va
   Scenario: Incluir registro ja cadastrados validacao apolice
      When consulto parametros de resseguro
      Then incluo registros cadastrados na validacao da apolice