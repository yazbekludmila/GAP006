from time import sleep
class PageLogin():

    def __init__(self, app):
        self.app = app

    def realizar_login(self):
        
        #self.app.clica_imagem(r'data\images\senha.PNG', similar=70)
        #if(getpass.getuser() == 'gsilvan'):
        #    self.app.escrever_direto('Mapfre2019')
        #elif(getpass.getuser() == 'jvictorr'):
        #    self.app.escrever_direto('@indra2018bb')
        #elif(getpass.getuser() == 'mconceicaos'):
        #    self.app.escrever_direto('automacao')
        #else:
        #    print('Usuario não reconhecido.')
        #self.app.digitos('enter')
        
        sleep(5)
        
        ## IMAGEM OK == USUARIO INEXISTENTE 
        self.app.combo_digitos('alt','f4')
        #self.app.digitos('enter')
        ##self.app.clica_imagem(r'data\images\oknaoexiste.png', similar=40)
        ##self.app.clica_imagem(r'data\images\ok_usernaoexiste.png', similar=40)
        ##self.app.clica_imagem(r'data\images\ok.png', similar=50)  
        #sleep(2)  

        self.app.digitos('tab')
        self.app.escrever_direto('ARODRIGUESSIL')
        self.app.digitos('tab')
        self.app.escrever_direto('mapfre2017')
        self.app.digitos('enter')
        sleep(5)

    def validacao_tela(self, imagem):
        tentativas = 50
        for tentativa in range(tentativas):
            if(self.app.verifica_tela(imagem, 60, similaridade=30) != None):
                break
            else:
                pass

    #def get_data_atual(self):
    #   data_atual = datetime.today().strftime('%d%m%Y')
    #   return data_atual

    #def get_data_futura(self):
    #    data_futura = (datetime.today() + relativedelta(years=1)).strftime('%d%m%Y')
    #    return data_futura


    
    #def selecionar_menu_modalidade_fraude(self):
    #        self.app.clica_imagem(r'data\images\procuramenu.png', similar=70)
    #        self.app.escrever_direto('modalidade de fraude')
    #        self.app.digitos('enter')      
    #        sleep(5)
                     
      
    #def selecionar_menu_gestao_Alerta(self):
        ##self.selecionar_menu_emissao('Menu de Atualizacoes')
    #        self.app.clica_imagem(r'data\images\procuramenu.png', similar=70)
    #        self.app.escrever_direto('gestao de alerta')
    #        self.app.digitos('enter')      
    #        sleep(5)       
                            

        ### TITULO DA TELA TRONWEB == APLICACAO MECANIZADA == PARA CONFIRMAR ENTROU TW OK 
        # self.app.clica_imagem(r'data\images\login-aceito.png', similar=70)
        ##self.tw.validacao_tela(imagem=r'data\images\premio_total.png')
        ### IMAGEM CAIXA TEXTO EM BRANCO (AZUL) LOCALIZAR == MENU DIGITAR MENU DESEJADO 
         
        #self.app.clica_imagem(r'data\images\step_1.png', similar=70)
        #self.app.escrever_direto('regras de alerta')
        #self.app.digitos('enter')
        #sleep(5)
        
        ### SELECIONANDO MENU == PELOS LINKS DOS MENUS ==> tronweb /sinistros /menu lcfo /regras alerta 
        #self.app.clica_imagem(r'data\images\MENUTW.png', similar=70, cliques=2)
        #sleep(5)
        #self.app.clica_imagem(r'data\images\MENUSINISTROS.png', similar=70, cliques=2)
        #sleep(5)
        #self.app.clica_imagem(r'data\images\menulcfo.png', similar=70, cliques=2) 
        #sleep(5)
        #self.app.clica_imagem(r'data\images\REGRASALERTALCFO.png', similar=70, cliques =2)
        #sleep(5)