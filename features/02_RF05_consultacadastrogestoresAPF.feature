@CadastroGestoresAPF

Feature: Manter Cadastro de Promotores - Gestores de Alertas de Possíveis Fraudes 
   Background: Estar logado no TW   
      Given que estou logado no sistema do tronweb 
   
   @CP001
   Scenario: consulta cadastro de gestores (APF) preenchendo usuário TW inválido e CTS válido 
      When selecionar menu promotor
      Then digitar TW INVALIDO CTS VALIDO e clicar BOTAO PESQUISAR
      When clicar x para fechar tela promotor
      Then tela promotores é fechada
      When clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado
   
   @CP002
   Scenario: consulta cadastro de gestores (APF) preenchendo usuário TW válido e CTS inválido
      When selecionar menu promotor
      Then digitar TW VALIDO CTS INVALIDO e clicar BOTAO PESQUISAR
      When clicar x para fechar tela promotor
      Then tela promotores é fechada
      When clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado
   
   @CP003
   Scenario: consulta cadastro de gestores (APF) sem preencher usuário TW e usuário CTS
      When selecionar menu promotor
      Then digitar TW BRANCO CTS ZERO e clicar BOTAO PESQUISAR
      When clicar x para fechar tela promotor
      Then tela promotores é fechada
      When clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado
   
   @CP004
   Scenario: consulta cadastro de gestores (APF) preenchendo usuário TW e CTS válido
      When selecionar menu promotor
      Then digitar TW VALIDO CTS VALIDO e clicar BOTAO PESQUISAR
      When clicar x para fechar tela promotor
      Then tela promotores é fechada
      When clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado
   
   @CP005
   Scenario: consulta cadastro de gestores de (APF) preenchendo CTS e TW inválidos
      When selecionar menu promotor
      Then digitar TW INVALIDO CTS INVALIDO e clicar BOTAO PESQUISAR
      When clicar x para fechar tela promotor
      Then tela promotores é fechada
      When clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado
   
   @CP006
   Scenario: inclui gestores preenchendo usuário CTS e TW e TODAS INFORMAÇÕES VALIDAS
      When selecionar menu promotor
      Then digitar TW VALIDO CTS VALIDO e clicar BOTAO PESQUISAR
      When clicar botao +
      And  alterar usuario tw  tipo  e ativo validos
      And  clicar botao NOVA ENTRADA e botao aceitar tela promotores
      And  clicar x para fechar tela promotor
      And  clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado
   
   @CP007
   Scenario: inclui gestores preenchendo TW INVALIDO E TIPO E ATIVO VALIDOS
      When selecionar menu promotor
      Then digitar TW VALIDO CTS VALIDO e clicar BOTAO PESQUISAR
      When clicar botao +
      And  alterar USUARIO TW INVALIDO e tipo e ativo validos
      Then exibir mensagem de erro
      When clicar botao Nova Entrada e botao aceitar tela promotores
      And  clicar x para fechar tela promotor
      And  clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado
   
   @CP008
   Scenario: inclui gestores preenchendo TIPO INVALIDO E TW E ATIVO VALIDOS
      When selecionar menu promotor
      Then digitar TW VALIDO CTS VALIDO e clicar BOTAO PESQUISAR
      When clicar botao +
      And  alterar TIPO INVALIDO E USUARIO E ATIVO validos
      Then exibir mensagem de erro
      When clicar botao Nova Entrada e botao aceitar tela promotores
      And  clicar x para fechar tela promotor
      And  clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado

   @CP009
   Scenario: inclui gestores preenchendo ATIVO INVALIDO E TW E TIPO VALIDOS 
      When selecionar menu promotor
      Then digitar TW VALIDO CTS VALIDO e clicar BOTAO PESQUISAR
      When clicar botao +
      And  alterar ATIVO INVALIDO E USUARIO E TIPO validos
      Then exibir mensagem de erro
      When clicar botao Nova Entrada e botao aceitar tela promotores
      And  clicar x para fechar tela promotor
      And  clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado

   @CP010
   Scenario: edita gestores preenchendo usuário CTS e TW e TODAS INFORMAÇÕES VALIDAS        
      When selecionar menu promotor
      Then digitar TW VALIDO CTS VALIDO e clicar BOTAO PESQUISAR
      When clicar botao lapis
      And  alterar usuario tw  tipo  e ativo validos
      And  clicar botao Aceitar e botao aceitar tela promotores
      When clicar x para fechar tela promotor
      Then tela promotores é fechada
      When clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado
      

   @CP011
   Scenario: edita gestores preenchendo TW  INVALIDO E TIPO E ATIVO VALIDOS  
      When selecionar menu promotor
      Then digitar TW VALIDO CTS VALIDO e clicar BOTAO PESQUISAR
      When clicar botao lapis
      And  alterar USUARIO TW INVALIDO e tipo e ativo validos
      Then exibir mensagem de erro
      When clicar botao Aceitar e botao aceitar tela promotores
      And  clicar x para fechar tela promotor
      And  clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado
   
   @CP012
   Scenario: edita gestores preenchendo  TIPO INVALIDO TW E ATIVO VALIDOS 
      When selecionar menu promotor
      Then digitar TW VALIDO CTS VALIDO e clicar BOTAO PESQUISAR
      When clicar botao lapis
      And  alterar TIPO INVALIDO E USUARIO E ATIVO validos
      Then exibir mensagem de erro
      When clicar botao Aceitar e botao aceitar tela promotores
      And  clicar x para fechar tela promotor
      And  clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado
   
   @CP013
   Scenario: edita gestores preenchendo ATIVO INVALIDO TW E TIPO VALIDOS
      When selecionar menu promotor
      Then digitar TW VALIDO CTS VALIDO e clicar BOTAO PESQUISAR
      When clicar botao lapis
      And  alterar ATIVO INVALIDO E USUARIO E TIPO validos 
      Then exibir mensagem de erro
      When clicar botao Aceitar e botao aceitar tela promotores
      And  clicar x para fechar tela promotor
      And  clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado
   
   