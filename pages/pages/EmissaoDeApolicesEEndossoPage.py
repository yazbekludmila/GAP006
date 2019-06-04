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
    
    def preencher_tomador(self,tomador, cnpj):
        self.app.clica_imagem(r'data\images\campo_tomador.png', similar=80)
        self.app.escrever_direto(tomador)
        self.app.digitos('tab')
        self.app.escrever_direto(cnpj)
        self.app.digitos('tab')
    
    def preencher_corret(self,corret):
        self.app.clica_imagem(r'data\images\campo_corret.png', similar=80)
        self.app.escrever_direto(corret)
        self.app.digitos('tab')
    
    def preencher_quadro_de_comissoes(self,quadro,comercial):
        self.app.clica_imagem(r'data\images\campo_corret.png', similar=80)
        self.app.escrever_direto(corret)
        self.app.digitos('tab')
        self.app.escrever_direto(corret)
        self.app.digitos('tab')
    
    def preencher_forma_de_pagto(self,pagto):
        self.app.clica_imagem(r'data\images\campo_forma_de_pagto.png', similar=80)
        self.app.escrever_direto(pagto)
        self.app.digitos('tab')
    
    def preencher_gestor_cobran(self,sigla_gestor, cod_gestor):
        self.app.clica_imagem(r'data\images\gestor_cobranca.png', similar=80)
        self.app.escrever_direto(sigla_gestor)
        self.app.digitos('tab')
        self.app.escrever_direto(cod_gestore)
    
    def clicar_continuar_emissao(self)
        self.app.clica_imagem(r'', similar=80)
    
    def preencher_num_da_proposta(self,num):
        self.app.digitos('tab')
        self.app.digitos('tab')
        self.app.digitos('tab')
        self.app.clica_imagem(r'data\images\mensagem_campo_obrigatorio.png', similar=80)
        self.app.clica_imagem(r'data\images\campo_numero_da_proposta .png', similar=80)
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
    
    def preencher_tipo_de_contratacao(self,tipo):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(tipo)
        self.app.digitos('tab')
    
    def preencher_grupo(self,grupo):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(grupo)
        self.app.digitos('tab')
    
    def preencher_tipo_de_risco(self,tipo):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(tipo)
        self.app.digitos('tab')
    
    def preencher_tipo_de_segmento(self,tipo):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(tipo)
        self.app.digitos('tab')
    
    def preencher_pontuacao(self,pontuacao):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(pontuacao)
        self.app.digitos('tab')
    
    def preencher_valor_em_risco_dm(self,valor):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(valor)
        self.app.digitos('tab')
    
    def preencher_percentual_de_dmp(self,percentual):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(percentual)
        self.app.digitos('tab')
    
    def preencher_percentual_de_pmp(self,percentual):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(percentual)
        self.app.digitos('tab')
    
    def preencher_classe_de_resseguro(self,classe):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(classe)
        self.app.digitos('tab')
    
    def preencher_vr_l_cessantes(self,valor):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(valor)
        self.app.digitos('tab')
    
    def preencher_tipo_de_seguro(self,seguro):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(seguro)
        self.app.digitos('tab')
    
    def preencher_risco_facultativo(self,risco):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(risco)
        self.app.digitos('tab')
    
    def preencher_cod_da_construcao(self,cod):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(cod)
        self.app.digitos('tab')
    
    def preencher_tipo_qualidade_da_construcao(self,tipo):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(tipo)
        self.app.digitos('tab')
    
    def preencher_protencionais(self,protencionais):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(protencionais)
        self.app.digitos('tab')
    
    def preencher_qualidade_do_risco(self,qualidade):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(qualidade)
        self.app.digitos('tab')
    
    def preencher_periodo_em_anos(self,anos):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(anos)
        self.app.digitos('tab')
    
    def preencher_percentual_de_sinistralidade(self,percentual):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(percentual)
        self.app.digitos('tab')

    def preencher_desc_agrav_tecnico(self,desc):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(desc)
        self.app.digitos('tab')
    
    def preencher_total_de_coberturas_para_calculo(self,total):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(total)
        self.app.digitos('tab')
    
    def preencher_seguro_ajustavel(self,seguro):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(valor)
        self.app.digitos('tab')
    
    def preencher_protecionais_roubo(self,protecionais):
        self.app.clica_imagem(r'', similar=80)
        self.app.escrever_direto(protecionais)
        self.app.digitos('tab')


    


    

        