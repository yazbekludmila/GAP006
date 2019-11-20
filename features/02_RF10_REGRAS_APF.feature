@CadastroRegrasAPF

Feature: Estruturação do Processo de Gestão de Alertas 
   Background: Estar logado no TW   
      Given que estou logado no sistema do tronweb
      
   @CP038
   Scenario: consulta regras de APF sem preencher ID e STATUS  
      When selecionar menu regras de alerta
      Then digitar ID ZERO STATUS BRANCO e clicar BOTAO PESQUISAR
      When clicar x para fechar tela REGRAS ALERTA
      Then tela alertas é fechada
      When clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado
   
   @CP039
   Scenario: consulta regras de APF preenchendo usuário ID inválido e STATUS válido
      When selecionar menu regras de alerta
      Then digitar ID INVALIDO STATUS VALIDO e clicar BOTAO PESQUISAR
      When clicar x para fechar tela REGRAS ALERTA
      Then tela alertas é fechada
      When clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado
   
   @CP040
   Scenario: consulta regras de APF preenchendo usuário ID válido e STATUS inválido
      When selecionar menu regras de alerta
      Then digitar ID VALIDO STATUS INVALIDO e clicar BOTAO PESQUISAR
      When clicar x para fechar tela REGRAS ALERTA
      Then tela alertas é fechada
      When clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado
   
   @CP041
   Scenario: consulta regras de APF preenchendo usuário ID válido e STATUS válido
      When selecionar menu regras de alerta
      Then digitar ID VALIDO STATUS VALIDO e clicar BOTAO PESQUISAR
      When clicar x para fechar tela REGRAS ALERTA
      Then tela alertas é fechada
      When clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado
   
   @CP042
   Scenario: inclui regras de APF preenchendo ALERTA INVALIDO E STATUS VALIDO
      When selecionar menu regras de alerta
      Then digitar ID VALIDO STATUS VALIDO e clicar BOTAO PESQUISAR
      When clicar botao +
      And  alterar ALERTA INVALIDO E STATUS VALIDO
      Then exibir mensagem de erro e fechar janela edicao
      When clicar ACEITAR e X E SIM tela alertas
      And  clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado
   
   @CP043
   Scenario: inclui regras de APF preenchendo ALERTA VALIDO E STATUS INVALIDO     
      When selecionar menu regras de alerta
      Then digitar ID VALIDO STATUS VALIDO e clicar BOTAO PESQUISAR
      When clicar botao +
      And  alterar ALERTA VALIDO E STATUS INVALIDO
      Then exibir mensagem de erro e fechar janela edicao
      When clicar ACEITAR e X E SIM tela alertas
      And  clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado
   
   @CP044
   Scenario: inclui regras de APF preenchendo ALERTA E STATUS VALIDOS
      When selecionar menu regras de alerta
      Then digitar ID VALIDO STATUS VALIDO e clicar BOTAO PESQUISAR
      When clicar botao +
      And  alterar ALERTA E STATUS VALIDOS
      And  clicar botao NOVA ENTRADA e botao aceitar tela alerta
      #And  clicar x para fechar tela REGRAS ALERTA
      Then tela alertas é fechada
      When clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado

   @CP045
   Scenario: edita regras de APF preenchendo ALERTA E STATUS VALIDOS
      When selecionar menu regras de alerta
      Then digitar ID VALIDO STATUS VALIDO e clicar BOTAO PESQUISAR
      When clicar botao lapis
      And  alterar ALERTA E STATUS VALIDOS
      And  clicar botao ACEITAR e botao aceitar tela alerta
      And  clicar x para fechar tela REGRAS ALERTA
      Then tela alertas é fechada
      When clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado
   
   @CP046
   Scenario: edita regras de APF preenchendo ALERTA INVALIDO E STATUS VALIDO
      When selecionar menu regras de alerta   
      Then digitar ID VALIDO STATUS VALIDO e clicar BOTAO PESQUISAR
      When clicar botao lapis
      And  alterar ALERTA INVALIDO E STATUS VALIDO
      Then exibir mensagem de erro e fechar janela edicao 
      When clicar ACEITAR e X E SIM tela alertas   
      And  clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado
   
   @CP047
   Scenario: edita regras de APF preenchendo ALERTA VALIDO E STATUS INVALIDO
      When selecionar menu regras de alerta
      Then digitar ID VALIDO STATUS VALIDO e clicar BOTAO PESQUISAR
      When clicar botao lapis
      And  alterar ALERTA VALIDO E STATUS INVALIDO
      Then exibir mensagem de erro e fechar janela edicao 
      When clicar ACEITAR e X E SIM tela alertas
      And  clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado
   
   @CP048
   Scenario: exclui regras de APF preenchendo ID e STATUS validos  
      When selecionar menu regras de alerta
      Then digitar ID VALIDO STATUS VALIDO e clicar BOTAO PESQUISAR
      When clicar botao X e botao aceitar tela alerta
      Then alerta selecionado será excluído
      When clicar x para fechar tela REGRAS ALERTA
      Then tela alertas é fechada
      When clicar x para fechar tela tw e clicar botao terminar
      Then tw é encerrado
