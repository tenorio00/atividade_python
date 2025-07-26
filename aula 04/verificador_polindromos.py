# Verificador de Palíndromos

import unicodedata

texto = input('Digite uma palavra ou frase: ')

# Remove acentos
def remover_acentos(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn')

# Remove espaços, pontuação e deixa tudo minúsculo
texto_limpo = ''.join(
    c.lower() for c in remover_acentos(texto)
    if c.isalnum()
)

if texto_limpo == texto_limpo[::-1]:
    print('Sim')
else:
    print('Não')

# Exemplo: "A cara rajada da jararaca" será reconhecida como palíndromo.