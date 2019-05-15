Feature: Consultar parâmetro de reasseguro

   Background: Login no sistema
      Given que usuario esta logado sistema com usuario valido
   
   @t
   Scenario: Consultar parâmetro de reasseguro   
      When consulto parametros de reasseguro
      Then tela com os campos preenchidos da pesquisa e exibido
   @r
   Scenario: Consultar parâmetro de reasseguro preenchendo somente ramo
      When consulto parametros de reasseguro preenchendo somente ramo
      Then mensagem de CAMPO OBRIGATORIO e exibido

   @p
   Scenario: Consultar parâmetro de reasseguro preenchendo somente produto
      When consulto parametros de reasseguro preenchendo somente produto
      Then mensagem de CAMPO OBRIGATORIO e exibido

   @nenhum
   Scenario: Consultar parâmetro de reasseguro sem preencher nenhum campo
      When consulto parametros de reasseguro sem preencher nenhum campo
      Then mensagem de CAMPO OBRIGATORIO e exibido

# given - dado
# when - quando
# then - então