import backend.api.integracao_front as integracao

def test_api_integracao():
    cadastro_data = {
        "nome":"hugo",
        "email": "hugo@email.com",
        "senha": "12345678/"
    }

    login_data = {
        "email": "hugo@email.com",
        "senha": "12345678/"
    }

    print("\nTeste de cadastro...")
    try:
        resposta = (integracao.cadastrar_usuario(cadastro_data))
        print(f"Resposta de Cadastro: {resposta}")
    except Exception as e:
        print(f"Erro no cadastro: {e}")

    print("\nTeste de login...")
    try:
        resposta = (integracao.login_usuario(login_data))
        print(f"Resposta de login: {resposta}")
    except Exception as e:
        print(f"Erro no login: {e}")

    print("\nTeste de listar livros...")
    try:
        resposta = (integracao.listar_livros())
        print(f"Resposta de listar livros: {resposta}")
    except Exception as e:
        print(f"Erro no listar livros: {e}")

    print("\nTeste de download do livro...")
    try:
        resposta = (integracao.realizar_download_livro(1, 1))
        print(f"Resposta de download do livro: {resposta}")
    except Exception as e:
        print(f"Erro no download do livro: {e}")

if __name__ == "__main__":
    test_api_integracao()