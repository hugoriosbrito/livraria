# Livraria Backend

Este projeto é o backend de uma livraria digital, responsável por gerenciar usuários, autenticação, listagem e download de livros.

## Como usar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute os testes de integração para validar a API:
   ```bash
   python teste_integracao.py
   ```

## Integração com o Frontend

O backend oferece as seguintes funcionalidades para integração:

### Cadastro de Usuário
```python
cadastrar_usuario({
    "nome": "nome_usuario",
    "email": "email@exemplo.com",
    "senha": "senha_segura"
})
```

### Login de Usuário
```python
login_usuario({
    "email": "email@exemplo.com",
    "senha": "senha_segura"
})
```

### Listagem de Livros
```python
listar_livros()
```

### Download de Livro
```python
realizar_download_livro(idLivro, idUsuario)
```

## Observações
- Certifique-se de que o backend Java (API principal) esteja rodando e acessível.
- A API se conecta ao endpoint base: http://api.livraria.spacenova.me
