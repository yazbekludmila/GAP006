Feature: Consultar parâmetro de reasseguro

   Background: Login no sistema
      Given que usuario esta logado sistema com usuario valido
   
   Scenario: Consultar parâmetro de reasseguro   
      When consulto parametros de reasseguro
      Then tela com os campos preenchidos da pesquisa e exibido

# given - dado
# when - quando
# then - então