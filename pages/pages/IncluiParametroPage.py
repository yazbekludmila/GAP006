from Pyautomators.desk import Desk
from Pyautomators.mouse_teclado import Teclado
from Pyautomators.mouse_teclado import Mouse
from pages.pages.TronWebPage import TronWeb
from data.data import Data

# Classes extras
from datetime import date
from time import sleep
from dateutil.relativedelta import relativedelta

class IncluiParametro():

    def __init__(self, app):
        self.app = app
        self.mouse = Mouse()
        self.teclado = Teclado()
        self.tron = TronWeb(self.app)
        self.data = Data(self.app)

    def inclui_parametro_re21(self):
        self.tron.validacao_tela(imagem=r'data\images\criar_registro.PNG')
        self.mouse.clica_imagem(r'data\images\criar_registro.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\criacao_modificacao_dados.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\cobertura.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\input_cobertura.PNG',similar=80)
        self.teclado.escrever_direto(self.data.cobertura())
        self.teclado.digitos('tab')
        self.teclado.digitos('tab')
        self.teclado.escrever_direto('10000')
        self.teclado.digitos('tab')
        self.teclado.escrever_direto(self.tron.get_data_atual())
        self.teclado.digitos('tab')
        self.teclado.escrever_direto(self.tron.get_data_futura())
        self.mouse.clica_imagem(r'data\images\aceitar3.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\vigencia_cadastrada.PNG',similar=80)

    def inclui_parametro_resseguro_invalido_re21(self):
        ### Exibe a msg "Em um campo numérico somente podem ser introduzidos numeros".
        self.mouse.clica_imagem(r'data\images\criar_registro.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\criacao_modificacao_dados.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\cobertura.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\input_cobertura.PNG',similar=80)
        self.teclado.escrever_direto('!@#$')
        self.teclado.digitos('tab')
        self.mouse.clica_imagem(r'data\images\msg_campo_numerico.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\botao_fechar.PNG',similar=80)

        ### Exibe a msg "VALOR INVALIDO".
        self.mouse.clica_imagem(r'data\images\criar_registro.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\criacao_modificacao_dados.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\ramo.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\input_ramo.PNG',similar=80)
        self.teclado.escrever_direto('0')
        self.teclado.digitos('tab')
        self.mouse.clica_imagem(r'data\images\msg_valor_invalido.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\botao_fechar.PNG',similar=80)

        ### Exibe a msg "COBERTURA INVALIDA PARA O PRODUTO".
        self.mouse.clica_imagem(r'data\images\criar_registro.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\criacao_modificacao_dados.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\cobertura.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\input_cobertura.PNG',similar=80)
        self.teclado.escrever_direto('0000')
        self.teclado.digitos('tab')
        self.mouse.clica_imagem(r'data\images\msg_cobertura_invalida.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\botao_fechar.PNG',similar=80)

        ### Exibe a msg "Em um campo numérico somente podem ser introduzidos numeros".
        self.mouse.clica_imagem(r'data\images\criar_registro.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\criacao_modificacao_dados.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\cobertura.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\input_cobertura.PNG',similar=80)
        self.teclado.escrever_direto('9999')
        self.teclado.digitos('tab')
        self.teclado.digitos('tab')
        self.teclado.escrever_direto('!@#$')
        self.teclado.digitos('tab')
        self.mouse.clica_imagem(r'data\images\msg_campo_numerico.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\botao_fechar.PNG',similar=80)

        ### Exibe a msg "Em um campo numérico somente podem ser introduzidos numeros".
        self.mouse.clica_imagem(r'data\images\criar_registro.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\criacao_modificacao_dados.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\cobertura.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\input_cobertura.PNG',similar=80)
        self.teclado.digitos('tab')
        self.teclado.digitos('tab')
        self.teclado.digitos('tab')
        self.teclado.escrever_direto('!@#$')
        self.mouse.clica_imagem(r'data\images\msg_campo_data.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\botao_fechar.PNG',similar=80)

        ### Exibe a msg "FORMATO NÃO VALIDO (ddMMyyyy)". - 
        self.mouse.clica_imagem(r'data\images\criar_registro.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\criacao_modificacao_dados.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\cobertura.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\input_cobertura.PNG',similar=80)
        self.teclado.digitos('tab')
        self.teclado.digitos('tab')
        self.teclado.digitos('tab')
        self.teclado.escrever_direto('00000000')
        self.teclado.digitos('tab')
        self.mouse.clica_imagem(r'data\images\msg_formato_nao_valido.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\botao_fechar.PNG',similar=80)


        ### Exibe a msg "FORMATO NÃO VALIDO (ddMMyyyy)". - 
        data_atual = date.today()
        data_atual = '{}0{}{}'.format(data_atual.day, data_atual.month, data_atual.year)
        self.mouse.clica_imagem(r'data\images\criar_registro.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\criacao_modificacao_dados.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\cobertura.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\input_cobertura.PNG',similar=80)
        self.teclado.digitos('tab')
        self.teclado.digitos('tab')
        self.teclado.digitos('tab')
        self.teclado.escrever_direto(data_atual)
        self.teclado.digitos('tab')
        self.teclado.escrever_direto('!@#!')
        self.mouse.clica_imagem(r'data\images\msg_campo_data.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\botao_fechar.PNG',similar=80)

        ### Exibe a msg "FORMATO NÃO VALIDO (ddMMyyyy)". - 
        self.mouse.clica_imagem(r'data\images\criar_registro.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\criacao_modificacao_dados.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\cobertura.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\input_cobertura.PNG',similar=80)
        self.teclado.digitos('tab')
        self.teclado.digitos('tab')
        self.teclado.digitos('tab')
        self.teclado.escrever_direto(data_atual)
        self.teclado.digitos('tab')
        self.teclado.escrever_direto('00-00-0000')
        self.mouse.clica_imagem(r'data\images\msg_campo_data.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\botao_fechar.PNG',similar=80)

        ### Exibe a msg "Em um campo numérico somente podem ser introduzidos numeros".
        self.mouse.clica_imagem(r'data\images\criar_registro.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\criacao_modificacao_dados.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\cobertura.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\input_cobertura.PNG',similar=80)
        self.teclado.digitos('tab')
        self.teclado.digitos('tab')
        self.teclado.digitos('tab')
        self.teclado.escrever_direto(data_atual)
        self.teclado.digitos('tab')
        self.teclado.escrever_direto('!@#$')
        self.mouse.clica_imagem(r'data\images\msg_campo_data.png',similar=80)
        self.mouse.clica_imagem(r'data\images\botao_fechar.PNG',similar=80)

        ### Exibe a msg "TAMANHO DO CAMPO INCORRETA".
        self.mouse.clica_imagem(r'data\images\criar_registro.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\criacao_modificacao_dados.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\cobertura.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\input_cobertura.PNG',similar=80)
        self.teclado.digitos('tab')
        self.teclado.digitos('tab')
        self.teclado.digitos('tab')
        self.teclado.escrever_direto(data_atual)
        self.teclado.digitos('tab')
        self.teclado.escrever_direto('2999')
        self.teclado.digitos('tab')
        self.mouse.clica_imagem(r'data\images\msg_tamanho_campo_incorreta.png',similar=80)
        self.mouse.clica_imagem(r'data\images\botao_fechar.PNG',similar=80)


    def inclui_parametro_resseguro_invalido_apolice(self):
        ### Exibe a msg "Em um campo numérico somente podem ser introduzidos numeros".
        self.mouse.clica_imagem(r'data\images\criar_registro.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\criacao_modificacao_dados.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\clique_validacao_apolice.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\ramo.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\input_ramo.PNG',similar=80)
        self.teclado.escrever_direto('!@#$')
        self.teclado.digitos('tab')
        self.mouse.clica_imagem(r'data\images\msg_campo_numerico.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\botao_fechar.PNG',similar=80)

        ### Exibe a msg "VALOR INVALIDO".
        self.mouse.clica_imagem(r'data\images\criar_registro.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\criacao_modificacao_dados.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\clique_validacao_apolice.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\ramo.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\input_ramo.PNG',similar=80)
        self.teclado.escrever_direto('0')
        self.teclado.digitos('tab')
        self.mouse.clica_imagem(r'data\images\aceitar3.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\msg_valor_invalido.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\botao_fechar.PNG',similar=80)

        ### Exibe a msg "VALOR INVALIDO".
        self.mouse.clica_imagem(r'data\images\criar_registro.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\criacao_modificacao_dados.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\clique_validacao_apolice.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\ramo.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\input_ramo.PNG',similar=80)
        self.teclado.escrever_direto('18')
        self.teclado.digitos('tab')
        self.teclado.escrever_direto('0')
        self.mouse.clica_imagem(r'data\images\aceitar3.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\msg_valor_invalido.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\botao_fechar.PNG',similar=80)

        ### Exibe a msg "Em um campo numérico somente podem ser introduzidos numeros".
        self.mouse.clica_imagem(r'data\images\criar_registro.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\criacao_modificacao_dados.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\clique_validacao_apolice.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\ramo.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\input_ramo.PNG',similar=80)
        self.teclado.escrever_direto('!@#$')
        self.teclado.digitos('tab')
        self.mouse.clica_imagem(r'data\images\aceitar3.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\msg_campo_numerico.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\botao_fechar.PNG',similar=80)

        ### Exibe a msg "Em um campo numérico somente podem ser introduzidos numeros".
        self.mouse.clica_imagem(r'data\images\criar_registro.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\criacao_modificacao_dados.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\clique_validacao_apolice.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\ramo.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\input_ramo.PNG',similar=80)
        self.teclado.escrever_direto('18')
        self.teclado.digitos('tab')
        self.teclado.escrever_direto('!@#$')
        self.mouse.clica_imagem(r'data\images\aceitar3.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\msg_campo_numerico.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\botao_fechar.PNG',similar=80)

    def inclui_registro_cadastrado_validacao_apolice(self):
        ### Exibe a msg "PRODUTO JÁ ESTA VALIDADO".
        self.mouse.clica_imagem(r'data\images\criar_registro.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\criacao_modificacao_dados.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\clique_validacao_apolice.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\ramo.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\input_ramo.PNG',similar=80)
        self.teclado.escrever_direto('18')
        self.teclado.digitos('tab')
        self.teclado.escrever_direto('117')
        self.mouse.clica_imagem(r'data\images\aceitar3.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\msg_produto_validado.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\botao_fechar.PNG',similar=80)

    def inclui_registro_cadastrado_enviar_re21(self):
        ### Exibe a msg "PRODUTO JÁ ESTA VALIDADO".
        self.mouse.clica_imagem(r'data\images\criar_registro.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\criacao_modificacao_dados.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\cobertura.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\input_cobertura.PNG',similar=80)
        self.teclado.escrever_direto('9999')
        self.teclado.digitos('tab')
        self.teclado.digitos('tab')
        self.teclado.digitos('tab')
        self.teclado.escrever_direto(data_atual)
        self.teclado.digitos('tab')
        self.teclado.escrever_direto(data_futura)
        self.mouse.clica_imagem(r'data\images\aceitar3.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\msg_vigencia_cadastrada.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\botao_fechar.PNG',similar=80)
