# Calculadora de Desconto em Produto

preco_original = float(input('Digite o preço original do produto: R$ '))
percentual_desconto = float(input('Digite o percentual de desconto: '))

valor_desconto = preco_original * (percentual_desconto / 100)
preco_final = preco_original - valor_desconto

print(f'Preço final com desconto: R$ {preco_final:.2f}')