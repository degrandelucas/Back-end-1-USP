import requests

response = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL')
print(response)

taxa_dolar = response.json()
taxa_dolar = float(taxa_dolar['USDBRL']['bid'])
print(type(taxa_dolar))

valor_em_real = float(input('Digite o valor em real (R$): '))
valor_em_dolar = valor_em_real / taxa_dolar

print(f'Valor em dólar: US$ {valor_em_dolar:.2f} | Cotação: R$ {taxa_dolar:.2f}')

