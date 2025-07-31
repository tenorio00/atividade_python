# Leitura de Arquivo CSV

import csv

arquivo = input('Digite o nome do arquivo CSV a ser lido: ')

try:
    with open(arquivo, mode='r', encoding='utf-8') as f:
        leitor = csv.reader(f)
        for linha in leitor:
            print(linha)
except FileNotFoundError:
    print('Arquivo não encontrado.')
except Exception as e:
    print('Erro ao ler o arquivo:', e)