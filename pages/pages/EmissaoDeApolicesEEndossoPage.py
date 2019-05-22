class EmissaoDeApolices():

    def __init__(self,app):
        self.app = app

    def preencher_campo_prod(self,prod):
        self.app.clica_imagem(r'data\images\campo_prod.png',similar=80)
        self.app.escrever_direto(prod)
        self.app.digitos('tab')
    
    def preencher_tipo_de_emissao(self, emissao):
        self.app.clica_imagem(r'data\images\campo_tipo_de_emissao.png',similar=80)
        self.app.escrever_direto(emissao)
        self.app.digitos('tab')
    
    def preencher_canal(self, canal):
        self.app.clica_imagem(r'data\images\campo_canal.png',similar=80)
        self.app.escrever_direto(canal)
        self.app.digitos('tab')
    
    def preencher_contrato(self, contrato):
        self.app.clica_imagem(r'data\images\campo_contrato.png',similar=80)
        self.app.escrever_direto(contrato)
        self.app.digitos('tab')
    
    def preencher_vigencia(self, vigencia):
        self.app.clica_imagem(r'data\images\campo_vigencia.png',similar=80)
        self.app.escrever_direto(vigencia)
        self.app.digitos('tab')
    
    def preencher_vigencia_final(self, final):
        self.app.clica_imagem(r'data\images\campo_vigencia_final.png',similar=80)
        self.app.escrever_direto(final)
        self.app.digitos('tab')
    
    def clicar_botao_prosseguir(self):
        self.app.clica_imagem(r'data\images\botao_prosseguir.png',similar=80)
    
    def preencher_tomador(self,tomador):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(tomador)
        self.app.digitos('tab')
    
    def preencher_quadro_de_distribuicao(self,quadro):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(quadro)
        self.app.digitos('tab')
    
    def preencher_forma_de_pagto(self,pagto):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(pagto)
        self.app.digitos('tab')
    
    def preencher_gestor_cobran(self,gestor):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(gestor)
        self.app.digitos('tab')
    
    def clicar_continuar_emissao(self)
        self.app.clica_imagem(r'', similar=80)
    
    def preencher_num_da_proposta(self,num):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(num)
        self.app.digitos('tab')
    
    def preencher_codigo_sistema_cooperativo(self,codigo):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(codigo)
        self.app.digitos('tab')
    
    def preencher_data_da_proposta(self,data):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(data)
        self.app.digitos('tab')
    
    def preencher_dia_venc_parcela(self,data):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(data)
        self.app.digitos('tab')
    
    def preencher_valida_fim_vig_parcelas(self, vigencia):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(vigencia)
        self.app.digitos('tab')
    
    def preencher_codigo_corretor_vera_cruz(self,cod):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(cod)
        self.app.digitos('tab')
    
    def preencher_comissao(self,comissao):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(comissao)
        self.app.digitos('tab')
    
    def preencher_orgao_publico(self,orgao):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(orgao)
        self.app.digitos('tab')
    
    def preencher_maior_valor_em_risco(self,valor):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(valor)
        self.app.digitos('tab')
    
    


    

        