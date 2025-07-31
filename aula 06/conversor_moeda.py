# Conversor de Moedas (para Reais - BRL)

import requests
from datetime import datetime

moeda = input('Digite o código da moeda estrangeira (ex: USD, EUR, GBP): ').strip().upper()
url = f'https://economia.awesomeapi.com.br/last/{moeda}-BRL'

try:
    resposta = requests.get(url, timeout=5)
    resposta.raise_for_status()
    dados = resposta.json()
    chave = f'{moeda}BRL'
    if chave not in dados:
        print('Código de moeda inválido ou não encontrado.')
    else:
        info = dados[chave]
        cotacao = float(info['bid'])
        maximo = float(info['high'])
        minimo = float(info['low'])
        data_hora = datetime.fromtimestamp(int(info['timestamp'])).strftime('%d/%m/%Y %H:%M:%S')

        print(f'Cotação atual: R$ {cotacao:.4f}')
        print(f'Valor máximo: R$ {maximo:.4f}')
        print(f'Valor mínimo: R$ {minimo:.4f}')
        print(f'Última atualização: {data_hora}')
except Exception as e:
    print('Erro ao consultar a cotação:', e)