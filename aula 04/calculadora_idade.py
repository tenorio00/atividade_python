# Calculadora de Idade em Dias

from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento: '))
ano_atual = date.today().year

idade_anos = ano_atual - ano_nascimento
idade_dias = idade_anos * 365

print(f'Idade aproximada em dias: {idade_dias}')