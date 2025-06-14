from backend.validacao.validacao import Validacao
from backend.api.requisicao import Endpoints, Requisicao

#INTEGRAÇÃO COM O FRONTEND

validacao = Validacao()

end = Endpoints(url_base="http://api.livraria.spacenova.me")
req = Requisicao(end)

def cadastrar_usuario(usuario: dict[str, str]):
    try:
        validacao.validar_email(usuario['email'])
    except Exception as e:
        raise Exception({e})

    try:
        validacao.validar_senha(usuario['senha'])
    except Exception as e:
        raise Exception(e)

    cadastro_banco = req.cadastrar(usuario)

    return cadastro_banco

def login_usuario(usuario: dict[str, str]):

    email_usuario = usuario['email']
    senha_usuario = usuario['senha']

    if not email_usuario or not senha_usuario:
        raise Exception("Email e senha são obrigatórios")

    login_banco = req.logar(usuario)

    return login_banco
    
def listar_livros():
    livros = req.listar_biblioteca()
    if not livros:
        raise Exception("Nenhum livro encontrado")
    return livros

def realizar_download_livro(idLivro, idUsuario):
    url_livro = req.realizar_download(idLivro, idUsuario)
    if not url_livro:
        raise Exception("Download do livro não encontrado")
    return url_livro

