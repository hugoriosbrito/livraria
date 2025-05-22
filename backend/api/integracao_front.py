from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional,


#API DE INTEGRAÇÃO COM O FRONTEND

app = FastAPI()

mock_usuarios = {}
mock_livros = [
    {"id": "1", "titulo": "O Senhor dos Anéis", "autor": "J.R.R. Tolkien"},
    {"id": "2", "titulo": "1984", "autor": "George Orwell"},
    {"id": "3", "titulo": "Dom Quixote", "autor": "Miguel de Cervantes"}
]
mock_carrinhos = {}
mock_pedidos = {}

# Models
class Usuario(BaseModel):
    id_usuario: str
    email: str
    senha: str

class Livro(BaseModel):
    id_livro: str
    titulo: str
    autor: str

class Pedido(BaseModel):
    id_pedido: str
    id_usuario: str

class CalculoFrete(BaseModel):
    id_usuario: str
    cep: str

class Validacao(BaseModel):
    id_usuario: str
    email: Optional[str] = None
    senha: Optional[str] = None
    endereco: Optional[str] = None

@app.post("/v1/usuario/cadastrar/")
async def cadastrar_usuario(usuario: Usuario):
    if usuario.id_usuario in mock_usuarios:
        raise HTTPException(status_code=400, detail="Usuário já existe")
    mock_usuarios[usuario.id_usuario] = {
        "email": usuario.email,
        "senha": usuario.senha
    }
    print(f"DEBUG: Stored user data: {mock_usuarios}")
    return {"message": "Usuário cadastrado com sucesso", "usuario": usuario}

@app.post("/v1/usuario/logar/")
async def login_usuario(usuario: Usuario):
    stored_user = mock_usuarios.get(usuario.id_usuario)
    if stored_user and stored_user["senha"] == usuario.senha:
        return {"message": "Login realizado com sucesso", "usuario": usuario}
    raise HTTPException(status_code=401, detail="Credenciais inválidas")

# Endpoints de livros
@app.get("/v1/livros/")
async def listar_biblioteca():
    return {"livros": mock_livros}

# Endpoints de carrinho
@app.post("/v1/loja/carrinho/adicionar/{idLivro}")
async def adicionar_ao_carrinho(idLivro: str):
    for livro in mock_livros:
        if livro["id"] == idLivro:
            if idLivro not in mock_carrinhos:
                mock_carrinhos[idLivro] = livro
            return {"message": f"Livro {idLivro} adicionado ao carrinho", "livro": livro}
    raise HTTPException(status_code=404, detail="Livro não encontrado")

@app.delete("/v1/loja/carrinho/remover/{idLivro}")
async def remover_do_carrinho(idLivro: str):
    if idLivro in mock_carrinhos:
        livro = mock_carrinhos.pop(idLivro)
        return {"message": f"Livro {idLivro} removido do carrinho", "livro": livro}
    raise HTTPException(status_code=404, detail="Livro não encontrado no carrinho")

# Endpoints de pedido
@app.post("/v1/loja/pedido/confirmar/{idPedido}")
async def confirmar_pedido(idPedido: str):
    if not mock_carrinhos:
        raise HTTPException(status_code=400, detail="Carrinho vazio")
    mock_pedidos[idPedido] = {
        "items": list(mock_carrinhos.values()),
        "status": "confirmado"
    }
    mock_carrinhos.clear()
    return {"message": f"Pedido {idPedido} confirmado", "pedido": mock_pedidos[idPedido]}

@app.delete("/v1/loja/pedido/cancelar/{idPedido}")
async def cancelar_pedido(idPedido: str):
    if idPedido in mock_pedidos:
        pedido = mock_pedidos.pop(idPedido)
        return {"message": f"Pedido {idPedido} cancelado", "pedido": pedido}
    raise HTTPException(status_code=404, detail="Pedido não encontrado")

# Endpoint de cálculo de prazo
@app.post("/v1/calculo/prazo-entrega/")
async def calcular_prazo_entrega(calculo: CalculoFrete):
    return {
        "endereco": "Endereço exemplo",
        "prazo_entrega": "3 dias úteis",
        "frete": 25.50
    }

# Endpoints de validação
@app.post("/v1/validar/email/")
async def validar_email(validacao: Validacao):
    return {"valid": True}

@app.post("/v1/validar/senha/")
async def validar_senha(validacao: Validacao):
    return {"valid": True}

@app.post("/v1/validar/pagamento/")
async def validar_pagamento(pedido: Pedido):
    return {"valid": True}

@app.post("/v1/validar/endereco/")
async def validar_endereco(validacao: Validacao):
    return {"valid": True}