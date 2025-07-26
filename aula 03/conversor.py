# Conversor de Temperatura

temperatura = float(input('Digite a temperatura: '))
origem = input('Unidade de origem (C, F ou K): ').strip().upper()
destino = input('Unidade de destino (C, F ou K): ').strip().upper()

resultado = None

if origem == 'C':
    if destino == 'F':
        resultado = (temperatura * 9/5) + 32
    elif destino == 'K':
        resultado = temperatura + 273.15
    elif destino == 'C':
        resultado = temperatura
elif origem == 'F':
    if destino == 'C':
        resultado = (temperatura - 32) * 5/9
    elif destino == 'K':
        resultado = (temperatura - 32) * 5/9 + 273.15
    elif destino == 'F':
        resultado = temperatura
elif origem == 'K':
    if destino == 'C':
        resultado = temperatura - 273.15
    elif destino == 'F':
        resultado = (temperatura - 273.15) * 9/5 + 32
    elif destino == 'K':
        resultado = temperatura

if resultado is not None:
    print(f'{temperatura} {origem} = {resultado:.2f} {destino}')
else:
    print('Conversão inválida.')