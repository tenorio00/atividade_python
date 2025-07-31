# Gerador de Senhas Seguras

import random
import string

tamanho = int(input('Digite o tamanho da senha desejada: '))

caracteres = string.ascii_letters + string.digits + '!@#$%&*'

senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

print('Senha gerada:', senha)