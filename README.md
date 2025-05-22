# Documentação do Backend da Livraria

Este documento descreve a estrutura e funcionamento do backend da livraria, um sistema que gerencia uma loja virtual de livros.

## Estrutura do Projeto

```
backend/
├── api/
│   ├── requisicao.py      # Cliente para comunicação com a API
│   └── integracao_front.py # API FastAPI para integração com o frontend
└── validacao/
    └── validacao.py       # Validações de dados
```

## Componentes Principais

### 1. API de Integração (integracao_front.py)

Este módulo implementa uma API REST usando FastAPI para integração com o frontend. 

#### Modelos de Dados
- `Usuario`: Dados do usuário (id, email, senha)
- `Livro`: Informações do livro (id, título, autor)
- `Pedido`: Dados do pedido
- `CalculoFrete`: Dados para cálculo de frete
- `Validacao`: Dados para validação

#### Endpoints Disponíveis

##### Usuários
- `POST /v1/usuario/cadastrar/`: Cadastro de novo usuário
- `POST /v1/usuario/logar/`: Login de usuário

##### Biblioteca
- `GET /v1/livros/`: Lista todos os livros disponíveis

##### Carrinho
- `POST /v1/loja/carrinho/adicionar/{idLivro}`: Adiciona livro ao carrinho
- `DELETE /v1/loja/carrinho/remover/{idLivro}`: Remove livro do carrinho

##### Pedidos
- `POST /v1/loja/pedido/confirmar/{idPedido}`: Confirma um pedido
- `DELETE /v1/loja/pedido/cancelar/{idPedido}`: Cancela um pedido

##### Validações
- `POST /v1/validar/email/`: Valida email
- `POST /v1/validar/senha/`: Valida senha
- `POST /v1/validar/pagamento/`: Valida pagamento
- `POST /v1/validar/endereco/`: Valida endereço

### 2. Cliente de Requisições (requisicao.py)

Este módulo fornece classes para fazer requisições HTTP para a API:

#### Classes
1. `Endpoints`
   - Gerencia URLs dos endpoints
   - Métodos para construir URLs para cada operação

2. `Requisicao`
   - Encapsula chamadas HTTP para a API
   - Métodos principais:
     - `cadastrar()`: Cadastro de usuário
     - `logar()`: Login de usuário
     - `listar_biblioteca()`: Lista livros
     - `adicionar_no_carrinho()`: Adiciona item ao carrinho
     - `remover_do_carrinho()`: Remove item do carrinho
     - `confirmar_pedido()`: Confirma pedido
     - `cancelar_pedido()`: Cancela pedido

### 3. Validações (validacao.py)

Módulo responsável pela validação de dados do usuário.

#### Classe `Validacao`
- Métodos estáticos para validação:
  - `validar_email()`: Valida formato de email
  - `validar_senha()`: Verifica requisitos de senha
  - `validar_endereco()`: Valida dados de endereço
  - `validar_numero_cartao()`: Valida número do cartão
  - `validar_data_expiracao_cartao()`: Valida data de expiração
  - `validar_cvv()`: Valida código CVV

## Testes

O projeto inclui dois arquivos de teste:

1. `teste_integracao.py`
   - Testa a integração entre os componentes
   - Verifica fluxo completo de operações

2. `teste-backend-api-requisicao.py`
   - Testes unitários para a API
   - Verifica cada endpoint individualmente

## Como Usar

### Configuração do Ambiente

1. Certifique-se de ter Python 3.x instalado
2. Instale as dependências:
   ```bash
   pip install fastapi requests email-validator
   ```

### Executando o Servidor

1. Inicie o servidor FastAPI:
   ```bash
   uvicorn backend.api.integracao_front:app --reload --port 8000
   ```

2. O servidor estará disponível em `http://localhost:8000`

## Observações

- O sistema usa mock data para demonstração
- Implementa validações robustas de dados
- Segue padrões REST para comunicação
- Possui tratamento de erros para casos comuns
