@given(u'que estou logado no sistema do tronweb')
def step_impl(context):
   
   #context.loginmenu.validacao_tela(imagem=r'data\images\ok_usernaoexiste.png')
   context.loginmenu.realizar_login()
   #context.loginmenu.validacao_tela(imagem=r'data\images\tron.PNG')









##@when(u'digitar promotor')
#def step_impl(context):
#   context.loginmenu.selecionar_menu_promotor()
##   context.gestoresapf.selecionar_menu01()

#@then(u'exibe menu de promotores')
#def step_impl(context):
#    pass

#@when(u'digitar modalidade de fraude')
#def step_impl(context):
#    context.loginmenu.selecionar_menu_modalidade_fraude()

#@then(u'exibe menu de modalidades de fraude')
#def step_impl(context):
#    pass

#@when(u'digitar gestao de alerta')
#def step_impl(context):
#    context.loginmenu.selecionar_menu_gestao_Alerta()

#@then(u'exibe menu de regras apf')
#def step_impl(context):
#    pass
