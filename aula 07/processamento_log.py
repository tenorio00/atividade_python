# Processamento de Logs de Treinamento

import pandas as pd

arquivo = input('Digite o nome do arquivo CSV: ')

try:
    df = pd.read_csv(arquivo)
    media = df['tempo_execucao'].mean()
    desvio = df['tempo_execucao'].std()
    print(f'Média do tempo de execução: {media:.2f}')
    print(f'Desvio padrão do tempo de execução: {desvio:.2f}')
except FileNotFoundError:
    print('Arquivo não encontrado.')
except Exception as e:
    print('Erro ao processar o arquivo:', e)