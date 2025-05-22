from backend.api.requisicao import Endpoints, Requisicao

def test_api():
    base_url = "http://localhost:8000"
    endpoints = Endpoints(base_url)
    req = Requisicao(endpoints)

    cadastro_data = {
        "id_usuario": "1",
        "email": "test@example.com",
        "senha": "123456"
    }
    print("\nTesting cadastro...")
    response = req.cadastrar(cadastro_data)
    print(f"Cadastro response: {response.json()}")

    # Test login
    print("\nTesting login...")
    response = req.logar(cadastro_data)
    print(f"Login response: {response.json()}")

    # Test listar biblioteca
    print("\nTesting listar biblioteca...")
    response = req.listar_biblioteca()
    print(f"Biblioteca response: {response.json()}")

    # Test adicionar no carrinho
    carrinho_data = {"idLivro": "1"}
    print("\nTesting adicionar no carrinho...")
    response = req.adicionar_no_carrinho(carrinho_data)
    print(f"Adicionar carrinho response: {response.json()}")

    # Test confirmar pedido
    pedido_data = {"idPedido": "1"}
    print("\nTesting confirmar pedido...")
    response = req.confirmar_pedido(pedido_data)
    print(f"Confirmar pedido response: {response.json()}")

if __name__ == "__main__":
    test_api()
