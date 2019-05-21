class CadastroApolice():

    def __init__(self,app):
        self.app = app
    
    def preencher_campo_apolice(self):
        self.app.clica_imagem(r'data\images\campo_numero_apolice.png', similar=70, cliques=2)
        self.app.escreve_direto(context.dados.numero_da_apolice())
