Feature: Consultar parâmetro de reasseguro

   Background: Login no sistema
      Given que usuario esta logado sistema com usuario valido
   
   Scenario: Consultar parâmetro de reasseguro   
      When consulto parametros de reasseguro
      Then tela com os campos preenchidos da pesquisa e exibido

   Scenario: Consultar parâmetro de reasseguro preenchendo somente ramo
      When consulto parametros de reasseguro preenchendo somente ramo
      Then mensagem de CAMPO OBRIGATORIO e exibido

   @p
   Scenario: Consultar parâmetro de reasseguro preenchendo somente produto
      When consulto parametros de reasseguro preenchendo somente produto
      Then mensagem de CAMPO OBRIGATORIO e exibido

# given - dado
# when - quando
# then - então