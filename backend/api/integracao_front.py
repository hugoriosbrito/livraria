from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib
from typing import List, Optional
import random
import uuid
from backend.validacao.validacao import Validacao
from backend.api.requisicao import Endpoints, Requisicao

#API DE INTEGRAÇÃO COM O FRONTEND

app = FastAPI()
validacao = Validacao()

end = Endpoints(url_base="http://localhost:9000")
req = Requisicao(end)

class Endereco(BaseModel):
    rua: str
    numero: str
    complemento: Optional[str] = None
    bairro: str
    cidade: str
    estado: str
    cep: str

class CadastroUsuario(BaseModel):
    id_usuario: Optional[str] = None
    nome: str
    email: str
    senha: str
    telefone: Optional[str] = None
    endereco: Endereco

class LoginUsuario(BaseModel):
    email: str
    senha: str

class Livro(BaseModel):
    idLivro: int
    titulo: str
    autor: str

class Pedido(BaseModel):
    id_pedido: str
    id_usuario: str

class CalculoFrete(BaseModel):
    cep: str


@app.post("/v1/usuario/cadastrar/")
async def cadastrar_usuario(usuario: CadastroUsuario):
    try:
        v_email = validacao.validar_email(usuario.email)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{e}")

    try:
        v_senha = validacao.validar_senha(usuario.senha)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"{e}")


    salt = "salt_de_teste"
    senha_usuario = usuario.senha+salt
    usuario.senha = str(hashlib.md5(senha_usuario.encode()).hexdigest())

    print("senha com hash: ", usuario.senha)

    usuario.id_usuario = str(uuid.uuid4())
    cadastro_banco = req.cadastrar(usuario.dict())

    return cadastro_banco

@app.post("/v1/usuario/logar/")
async def login_usuario(usuario: LoginUsuario):

    email_usuario = usuario.email
    senha_usuario = usuario.senha

    salt = "salt_de_teste"
    senha_usuario = senha_usuario+salt
    usuario.senha = str(hashlib.md5(senha_usuario.encode()).hexdigest())
    senha_usuario = usuario.senha

    print("senha com hash: ", usuario.senha)

    if not email_usuario or not senha_usuario:
        raise HTTPException(status_code=400, detail="Email e senha são obrigatórios")

    login_banco = req.logar(usuario.dict())
    return login_banco
    

@app.get("/v1/livros/")
async def listar_livros():
    livros = req.listar_biblioteca()
    if not livros:
        raise HTTPException(status_code=404, detail="Nenhum livro encontrado")
    return livros

# Endpoints de carrinho
@app.post("/v1/loja/carrinho/adicionar/{idLivro}")
async def adicionar_ao_carrinho(idLivro: int):
    if not idLivro:
        raise HTTPException(status_code=400, detail="ID do livro é obrigatório")
    
    banco_adicionar_livro_carrinho = req.adicionar_no_carrinho(idLivro)
    return banco_adicionar_livro_carrinho

@app.delete("/v1/loja/carrinho/remover/{idLivro}")
async def remover_do_carrinho(idLivro: int):
    if not idLivro:
        raise HTTPException(status_code=400, detail="ID do livro é obrigatório")
    
    banco_remover_livro_carrinho = req.remover_do_carrinho(idLivro)
    return banco_remover_livro_carrinho

# Endpoints de pedido
# quando o usuario cria o pedido, é sintetizado todo o carrinho em um só pedido com um id, e assim o usuário pode confirmar ou cancelar
@app.get("/v1/loja/pedido/criar/")
async def criar_pedido_():
    idPedido = str(uuid.uuid1())
    banco_criar_pedido = req.criar_pedido(idPedido)
    return banco_criar_pedido

@app.post("/v1/loja/pedido/confirmar/{idPedido}")
async def confirmar_pedido(idPedido: str):
    if not idPedido:
        raise HTTPException(status_code=400, detail="ID do pedido é obrigatório")
    
    banco_confirmar_pedido = req.confirmar_pedido(idPedido)
    return banco_confirmar_pedido

@app.delete("/v1/loja/pedido/cancelar/{idPedido}")
async def cancelar_pedido(idPedido: str):
    if not idPedido:
        raise HTTPException(status_code=400, detail="ID do pedido é obrigatório")
    
    banco_cancelar_pedido = req.cancelar_pedido(idPedido)
    return banco_cancelar_pedido

    
"""
# Endpoint de cálculo de prazo
@app.post("/v1/calculo/prazo-entrega/")
async def calcular_prazo_entrega(calculo: CalculoFrete):
    prazo_entrega = int(random.randint(1,10))
    frete = format(float(random.uniform(10.0, 50.0)), '.2f')
    print(prazo_entrega)
    return {
        "prazo_entrega": f"{prazo_entrega} dias úteis",
        "frete": frete
    }
"""