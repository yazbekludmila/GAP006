from time import sleep
class MenuGestaoAlerta():

    def __init__(self, app):
        self.app = app

    def seleciona_menu_gestao_alerta(self):
                 
        self.app.clica_imagem(r'data\images\procuramenu.png', similar=70)
        self.app.escrever_direto('gestao de alerta')
        self.app.digitos('enter')
        sleep(5)
        
        ### SELECIONANDO MENU == PELOS LINKS DOS MENUS ==> tronweb /sinistros /menu lcfo /regras alerta 
        #self.app.clica_imagem(r'data\images\MENUTW.png', similar=70, cliques=2)
        #sleep(5)
        #self.app.clica_imagem(r'data\images\MENUSINISTROS.png', similar=70, cliques=2)
        #sleep(5)
        #self.app.clica_imagem(r'data\images\menulcfo.png', similar=70, cliques=2) 
        #sleep(5)
        #self.app.clica_imagem(r'data\images\REGRASALERTALCFO.png', similar=70, cliques =2)
        #sleep(5)