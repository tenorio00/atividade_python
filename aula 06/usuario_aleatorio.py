# Gerador de Usuário Aleatório

import requests

try:
    resposta = requests.get('https://randomuser.me/api/', timeout=5)
    resposta.raise_for_status()
    dados = resposta.json()
    usuario = dados['results'][0]
    nome = f"{usuario['name']['first']} {usuario['name']['last']}"
    email = usuario['email']
    pais = usuario['location']['country']

    print('Nome:', nome)
    print('E-mail:', email)
    print('País:', pais)
except Exception as e:
    print('Erro ao acessar a API:', e)