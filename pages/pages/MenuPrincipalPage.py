from Pyautomators.mouse_teclado import Teclado
from Pyautomators.mouse_teclado import Mouse
from Pyautomators.Verifica import Valida

class  MenuPrincipal():

    def __init__(self, app):
        self.app = app
        self.mouse = Mouse()
        self.teclado = Teclado()
        self.asserts = Valida()
    
    def abrir_emissao(self):
        self.mouse.clica_imagem(r'data\images\opcao_tronweb.png', similar=70, cliques=2)
        self.asserts.verifica_tela(r'data\images\opcao_emissao.png', 80, similaridade=50)
        self.mouse.clica_imagem(r'data\images\opcao_emissao.png', similar=70, cliques=2)
    
    def selecionar_menu_emissao(self,opcao):
        self.mouse.clica_imagem(r'data\images\botao_direita.png', similar=70, cliques=1)
        if(opcao == 'Menu de Atualizacoes'):
            self.mouse.clica_imagem(r'data\images\opcao_menu_de_atualizacoes.png', similar=70, cliques=2)
        elif(opcao == 'Emissao Apolices Endossos'):
            self.mouse.clica_imagem(r'data\images\opcao_emissao_de_apolices.png', similar=70, cliques=2)
    
    def clicar_cadastro_apolice(self):
        self.mouse.clica_imagem(r'data\images\baixo.png', similar=70, cliques=14)
        self.mouse.clica_imagem(r'data\images\botao_direita.png', similar=70, cliques=1)
        self.mouse.clica_imagem(r'data\images\cadastro_apolice.png', similar=70, cliques=2)
    
    def validar_tela_cadastro_apolices(self):
        while(Valida.verifica_tela(r"data\images\campo_numero_apolice.png", 80, similaridade=50) == None):
            if(Valida.verifica_tela(r"data\images\campo_numero_apolice.png", 80, similaridade=50) != None):
                break
            else:
                pass
    
    def preencher_campo_apolice(self,numero):
        self.mouse.clica_imagem(r'data\images\campo_numero_apolice.png', similar=70)
        self.teclado.escrever_direto(numero)

    def validar_tela_emissao_apolices(self):
        while(Valida.verifica_tela(r"data\images\validar_apolice_cliente.png", 80, similaridade=50) == None):
            if(Valida.verifica_tela(r"data\images\validar_apolice_cliente.png", 80, similaridade=50) != None):
                break
            else:
                pass
    
    def preencher_campo_prod(self):
        self.mouse.clica_imagem(r'data\images\campo_prod.png', similar=70)
        self.teclado.escrever_direto('117')

    def preencher_campo_tipo_de_emissao(self):
        self.mouse.clica_imagem(r'data\images\campo_tipo_de_emissao.png', similar=70)
        self.teclado.escrever_direto('P')
        self.teclado.digitos('TAB')
    
    def preencher_campo_canal(self):
        self.mouse.clica_imagem(r'data\images\campo_canal.png', similar=70)
        self.teclado.escrever_direto('99')
    
