from datetime import date
from datetime import datetime
from dateutil.relativedelta import relativedelta

data_atual = date.today()
data_em_texto = '{}0{}{}'.format(data_atual.day, data_atual.month, data_atual.year)

print(data_em_texto)

print('**********************************************')

data_futura = date.today() + relativedelta(years=1)
data_futura = '{}0{}{}'.format(data_futura.day, data_futura.month, data_futura.year)
print(data_futura)