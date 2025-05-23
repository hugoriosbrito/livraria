import requests
import json


def test_api_integracao():
    cadastro_data = {
        "nome": "hugo",
        "email": "hugo@email.com",
        "senha": "12345678/",
        "telefone": "71555555555",
        "endereco": {
            "rua": "rua do chapéu",
            "numero": "829",
            "complemento": "",
            "bairro": "cartola",
            "cidade": "Salvador",
            "estado": "Bahia",
            "cep": "49650800"
        }
    }

    login_data = {
        "email": "hugo@email.com",
        "senha": "12345678/"
    }

    print("\nTeste de cadastro...")
    try:
        response = requests.post("http://localhost:8000/v1/usuario/cadastrar/", json=cadastro_data)
        print(f"Status: {response.status_code}")
        print(f"Resposta de Cadastro: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Erro no cadastro: {e}")

    import time
    time.sleep(2) # para garantir que o cadastro foi feito antes de logar, as vezes da erro

    print("\nTeste de login...")
    try:
        response = requests.post("http://localhost:8000/v1/usuario/logar/", json=login_data)
        print(f"Status: {response.status_code}")
        print(f"Resposta de Login: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Erro no login: {e}")

    print("\nTeste listar biblioteca...")
    try:
        response = requests.get("http://localhost:8000/v1/livros/")
        print(f"Status: {response.status_code}")
        print(f"Resposta Lista Biblioteca: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao listar biblioteca: {e}")

    print("\nTeste adicionar no carrinho 1...")
    idLivro = 1
    try:
        response = requests.post(f"http://localhost:8000/v1/loja/carrinho/adicionar/{idLivro}")
        print(f"Status: {response.status_code}")
        print(f"Resposta de adicionar carrinho: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao adicionar no carrinho: {e}")

    print("\nTeste adicionar no carrinho 2...")
    idLivro = 2
    try:
        response = requests.post(f"http://localhost:8000/v1/loja/carrinho/adicionar/{idLivro}")
        print(f"Status: {response.status_code}")
        print(f"Resposta de adicionar carrinho: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao adicionar no carrinho: {e}")
        
    print("\nTeste adicionar no carrinho 3...")
    idLivro = 3
    try:
        response = requests.post(f"http://localhost:8000/v1/loja/carrinho/adicionar/{idLivro}")
        print(f"Status: {response.status_code}")
        print(f"Resposta de adicionar carrinho: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao adicionar no carrinho: {e}")

    print("\nTeste remover do carrinho...")
    idLivroRemover = 1
    try:
        response = requests.delete(f"http://localhost:8000/v1/loja/carrinho/remover/{idLivroRemover}")
        print(f"Status: {response.status_code}")
        print(f"Resposta de remover carrinho: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao remover do carrinho: {e}")

    print("\nTeste criar pedido...")
    try:
        response_criar_pedido = requests.get("http://localhost:8000/v1/loja/pedido/criar/")
        print(f"Status: {response_criar_pedido.status_code}")
        print(f"Resposta de criar pedido: {response_criar_pedido.text}")
        
        if response_criar_pedido.status_code == 200:
            try:
                pedido_data = response_criar_pedido.json()
                data = pedido_data.get("data", {})
                idPedido = data.get("idPedido")
            except json.JSONDecodeError:
                print("erro: Resposta não é um json")
                idPedido = None
        else:
            idPedido = None
    except requests.exceptions.RequestException as e:
        print(f"Erro ao criar pedido: {e}")
        idPedido = None

    if idPedido:
        print(f"\nID do pedido criado: {idPedido}")
        
        print("\nTeste de confirmar pedido...") 
        try:
            response = requests.post(f"http://localhost:8000/v1/loja/pedido/confirmar/{idPedido}")
            print(f"Status: {response.status_code}")
            print(f"Resposta de confirmar pedido: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"erro ao confirmar pedido: {e}")

        print("\nTeste de cancelar pedido...")
        try:
            response = requests.delete(f"http://localhost:8000/v1/loja/pedido/cancelar/{idPedido}")
            print(f"Status: {response.status_code}")
            print(f"Resposta de cancelar pedido: {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Erro ao cancelar pedido: {e}")
    else:
        print("\nNão foi possível obter ID do pedido. Testes de confirmar e cancelar não vão ser feitos.")


if __name__ == "__main__":
    test_api_integracao()