import requests

def consultar_cep(cep):
    if not (cep.isdigit() and len(cep) == 8):
        print('CEP inválido. Digite exatamente 8 números.')
        return

    url = f'https://viacep.com.br/ws/{cep}/json/'
    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()

        if 'erro' in dados:
            print('CEP não encontrado.')
        else:
            print('Logradouro:', dados.get('logradouro', ''))
            print('Bairro:', dados.get('bairro', ''))
            print('Cidade:', dados.get('localidade', ''))
            print('Estado:', dados.get('uf', ''))
            print('CEP:', dados.get('cep', ''))
    except requests.RequestException:
        print('Erro de conexão ao consultar o CEP.')
    except Exception as e:
        print('Erro ao consultar o CEP:', e)

if __name__ == "__main__":
    cep = input('Digite o CEP (apenas números): ').strip()
    consultar_cep(cep)