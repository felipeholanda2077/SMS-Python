#Pandas

import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACbe71ac924833b3b886b7714510009177"
# Your Auth Token from twilio.com/console
auth_token  = "80a780331629588883837ace54be75a4"
client = Client(account_sid, auth_token)

# Abrir os 6 arquivos em excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+5511953528042",
            from_="+18305496883",
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)


# Para cada arquvio:

# Verificar se algum valor na coluna vendas daquele é maior que 55 mil

# Se for maior que 55 mil -> Envia um SMS com o Nome, o mês e as vendas do vendedor

# Caso não seja maior que 55.000 não fazer nada
