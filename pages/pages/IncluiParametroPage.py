from Pyautomators.desk import Desk
from Pyautomators.mouse_teclado import Teclado
from Pyautomators.mouse_teclado import Mouse

# Classes extras
from datetime import date
from time import sleep
from dateutil.relativedelta import relativedelta

class IncluiParametro():

    def __init__(self, app):
        self.app = app
        self.mouse = Mouse()
        self.teclado = Teclado()

    def inclui_parametro(self):
        self.mouse.clica_imagem(r'data\images\criar_registro.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\criacao_modificacao_dados.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\cobertura.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\input_cobertura.PNG',similar=80)
        # sleep(10)
        self.teclado.escrever_direto('9999')
        self.teclado.digitos('tab')
        self.teclado.digitos('tab')
        self.teclado.escrever_direto('10000')
        self.teclado.digitos('tab')
        ### Formata a data no formato correto
        data_atual = date.today()
        data_atual = '{}0{}{}'.format(data_atual.day, data_atual.month, data_atual.year)
        data_futura = date.today() + relativedelta(years=1)
        data_futura = '{}0{}{}'.format(data_futura.day, data_futura.month, data_futura.year)

        self.teclado.escrever_direto(data_atual)
        self.teclado.digitos('tab')
        self.teclado.escrever_direto(data_futura)
        self.mouse.clica_imagem(r'data\images\aceitar3.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\vigencia_cadastrada.PNG',similar=80)

    def inclui_parametro_resseguro_invalido(self):
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
        # self.teclado.digitos('tab')
        self.mouse.clica_imagem(r'data\images\msg_campo_data.PNG',similar=80)
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
        self.teclado.escrever_direto('00-00-0000')
        # self.teclado.digitos('tab')
        self.mouse.clica_imagem(r'data\images\msg_campo_data.PNG',similar=80)
        self.mouse.clica_imagem(r'data\images\botao_fechar.PNG',similar=80)

        ### Exibe a msg "Em um campo numérico somente podem ser introduzidos numeros".
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
        self.teclado.escrever_direto('!@#$')
        # self.teclado.digitos('tab')
        self.mouse.clica_imagem(r'data\images\msg_campo_data.png',similar=80)
        self.mouse.clica_imagem(r'data\images\botao_fechar.PNG',similar=80)

        ### Exibe a msg "TAMANHO DO CAMPO INCORRETA".
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
        self.teclado.escrever_direto('2999')
        self.teclado.digitos('tab')
        self.mouse.clica_imagem(r'data\images\msg_tamanho_campo_incorreta.png',similar=80)
        self.mouse.clica_imagem(r'data\images\botao_fechar.PNG',similar=80)



