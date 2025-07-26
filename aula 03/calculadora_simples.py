# Calculadora Simples

while True:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    operacao = input('Digite a operação desejada (+, -, *, /): ')

    resultado = None

    if operacao == '+':
        resultado = num1 + num2
    elif operacao == '-':
        resultado = num1 - num2
    elif operacao == '*':
        resultado = num1 * num2
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 / num2
        else:
            print('Erro: divisão por zero!')
    else:
        print('Operação inválida!')

    if resultado is not None:
        print(f'Resultado: {resultado}')
        break