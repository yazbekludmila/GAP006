from pages.pages.TronWebPage import TronWeb as tw
import time
import random

class EmissaoDeApolices():

    def __init__(self,app):
        self.app = app
        self.tw = tw(self.app)

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
    
    def carregar_numero_de_cotacao(self):
        self.app.clica_imagem(r'data\images\campo_numero_cotacao.png',similar=80)
        self.app.digitos('tab')
    
    def preencher_vigencia(self, vigencia):
        #self.app.clica_imagem(r'data\images\campo_vigencia.png',similar=80)
        self.app.digitos('tab')
        self.app.digitos('tab')
        self.app.digitos('tab')
        self.app.digitos('tab')
        self.app.digitos('tab')
    
    def clicar_botao_prosseguir(self):
        self.app.clica_imagem(r'data\images\botao_prosseguir.png',similar=80)
    
    def preencher_tomador(self,tomador,cnpj):
        self.app.digitos('tab')
        self.app.digitos('tab')
        self.app.clica_imagem(r'data\images\campo_tomador.png', similar=80)
        self.app.escrever_direto(tomador)
        self.app.digitos('tab')
        self.app.escrever_direto(cnpj)
        self.app.digitos('tab')
    
    def preencher_corret(self,corret):
        self.app.digitos('tab')
        self.app.clica_imagem(r'data\images\campo_corretagem.png', similar=80)
        self.app.escrever_direto(corret)
        
    
    def preencher_quadro_de_comissoes(self,quadro,comercial):
        #self.app.clica_imagem(r'data\images\campo_quadro_de_comissoes.png', similar=80)
        self.app.digitos('tab')
        self.app.escrever_direto(quadro)
        self.app.digitos('tab')
        self.app.escrever_direto(comercial)
        self.app.digitos('tab')
        self.app.clica_imagem(r'data\images\campo.png', similar=80)
        self.app.clica_imagem(r'data\images\botao_aceitar.png', similar=80)
    
    def preencher_forma_de_pagto(self,pagto):
        self.app.clica_imagem(r'data\images\campo_forma_de_pagto.png', similar=80)
        self.app.escrever_direto(pagto)
        self.app.digitos('tab')
        self.app.digitos('tab')
    
    def preencher_gestor_cobran(self,sigla_gestor, cod_gestor):
        self.app.clica_imagem(r'data\images\gestor_cobranca.png', similar=80)
        self.app.escrever_direto(sigla_gestor)
        self.app.digitos('tab')
        self.app.escrever_direto(cod_gestor)
    
    def clicar_continuar_emissao(self):
        self.app.clica_imagem(r'data\images\botao_continua_emissao.png', similar=80)
    
    def preencher_num_da_proposta(self):
        self.app.digitos('f12')
        num = '99{number}'.format(number=str(random.randint(100000,999999)))
        time.sleep(4)
        self.tw.validacao_tela(imagem=r'data\images\campo_numero_da_proposta.png')
        self.app.digitos('f12')
        #vself.app.clica_imagem(r'data\images\campo_azul.png', similar=80, cliques=3)
        self.app.escrever_direto(num)
        self.app.digitos('f12')
    
    def classe_resseguro(self, classe):
        self.app.clica_imagem(r'data\images\classe_resseguro.png', similar=80)
        self.app.escrever_direto(classe)
        self.app.digitos('tab')

    def codigo_corretor_veracruz(self, codigo):
        self.app.digitos('f12')
        self.tw.validacao_tela(imagem=r'data\images\codigo_corretor_veracruz.png')
        self.app.escrever_direto(codigo)
        self.app.digitos('f12')
    
    def comissao(self, comissao):
        self.app.digitos('f12')
        self.tw.validacao_tela(imagem=r'data\images\comissao.png')
        self.app.escrever_direto(comissao)
        self.app.digitos('f12')
        time.sleep(4)
        self.app.clica_imagem(r'data\images\espaco.png', similar=80)
        time.sleep(4)
        self.app.clica_imagem(r'data\images\botao_baixo2.png', similar=80)

    def data_proposta(self, proposta):
        self.app.digitos('f12')
        self.tw.validacao_tela(imagem=r'data\images\data_proposta.png')
        self.app.digitos('f12')
        self.app.digitos('tab')
        self.app.escrever_direto(proposta)
        self.app.digitos('f12')

    def dia_vencimento_parcela(self, data):
        self.app.digitos('f12')
        self.tw.validacao_tela(imagem=r'data\images\dia_vencimento_parcela.png')
        self.app.clica_imagem(r'data\images\dia_vencimento_parcela.png', similar=80)
        self.app.escrever_direto(data)
        self.app.digitos('f12')
        time.sleep(2)
        self.app.digitos('tab')


    def numero_proposta(self, numero):
        self.app.clica_imagem(r'data\images\numero_proposta.png', similar=80)
        self.app.escrever_direto(numero)
        self.app.digitos('tab')

    def percentual_de_dmp(self, percentual_de_dmp):
        self.app.clica_imagem(r'data\images\percentual_de_dmp.png', similar=80)
        self.app.escrever_direto(percentual_de_dmp)
        self.app.digitos('tab')

    def percentual_de_pmp(self, percentual_de_pmp):
        self.app.clica_imagem(r'data\images\percentual_de_pmp.png', similar=80)
        self.app.escrever_direto(percentual_de_pmp)
        self.app.digitos('tab')

    def pontuacao(self, pontuacao):
        self.app.clica_imagem(r'data\images\pontuacao.png', similar=80)
        self.app.escrever_direto(pontuacao)
        self.app.digitos('tab')

    def premio_total(self, premio):
        time.sleep(3)
        self.tw.validacao_tela(imagem=r'data\images\premio_total.png')
        self.app.digitos('f12')
        self.app.escrever_direto(premio)
        self.app.digitos('f12')

    def texto_para_descricao(self, texto):
        self.app.clica_imagem(r'data\images\texto_para_descricao.png', similar=80)
        self.app.escrever_direto(texto)
        self.app.digitos('tab')

    def tipo_de_contratacao(self, tipo):
        self.app.clica_imagem(r'data\images\tipo_de_contratacao.png', similar=80)
        self.app.escrever_direto(tipo)
        self.app.digitos('tab')

    def tipo_de_risco(self, tipo):
        self.app.clica_imagem(r'data\images\tipo_de_risco.png', similar=80)
        self.app.escrever_direto(tipo)
        self.app.digitos('tab')

    def tipo_de_seguro(self, tipo):
        self.app.clica_imagem(r'data\images\tipo_de_seguro.png', similar=80)
        self.app.escrever_direto(tipo)
        self.app.digitos('tab')

    def valor_em_risco(self, valor):
        self.app.clica_imagem(r'data\images\valor_em_risco.png', similar=80)
        self.app.escrever_direto(valor)
        self.app.digitos('tab')

    def vr_cessantes(self, vr_cessantes):
        self.app.clica_imagem(r'data\images\vr_cessantes.png', similar=80)
        self.app.escrever_direto(vr_cessantes)
        self.app.digitos('tab')
    


    

        