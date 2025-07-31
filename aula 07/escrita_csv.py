# Escrita de Arquivo CSV

import csv

# Lista de listas com dados fictícios
dados = [
    ['João', 30, 'São Paulo'],
    ['Maria', 25, 'Belo Horizonte'],
    ['Carlos', 40, 'Rio de Janeiro']
]

arquivo = input('Digite o nome do arquivo CSV para salvar os dados: ')

try:
    with open(arquivo, mode='w', newline='', encoding='utf-8') as f:
        escritor = csv.writer(f)
        escritor.writerow(['nome', 'idade', 'cidade'])
        escritor.writerows(dados)
    print(f'Dados gravados com sucesso em "{arquivo}".')
except Exception as e:
    print('Erro ao gravar o arquivo:', e)