# Leitura e Escrita de Arquivo JSON

import json

# Cria um dicionário com dados fictícios
pessoa = {
    'nome': 'Lucas',
    'idade': 29,
    'cidade': 'Curitiba'
}

arquivo = input('Digite o nome do arquivo JSON: ')

# Salva o dicionário no arquivo JSON
try:
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(pessoa, f, ensure_ascii=False, indent=4)
    print(f'Dados salvos em "{arquivo}".')
except Exception as e:
    print('Erro ao salvar o arquivo:', e)

# Lê o arquivo JSON e exibe os dados
try:
    with open(arquivo, 'r', encoding='utf-8') as f:
        dados = json.load(f)
    print('Dados carregados do arquivo:')
    print(dados)
except FileNotFoundError:
    print('Arquivo não encontrado.')
except Exception as e:
    print('Erro ao ler o arquivo:', e)