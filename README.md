# Documentação do Backend da Livraria

Este documento descreve a estrutura e funcionamento do backend da livraria, um sistema que gerencia uma loja virtual de livros com foco em literatura LGBTQ+.

## Estrutura do Projeto

```
backend/
├── api/
│   ├── requisicao.py      # Lógica de negócio e mock data
│   └── integracao_front.py # API FastAPI para integração com o frontend
└── validacao/
    └── validacao.py       # Validações de dados
```

## Componentes Principais

### 1. API de Integração (integracao_front.py)

Este módulo implementa uma API REST usando FastAPI para integração com o frontend. O sistema utiliza autenticação por hash MD5 com salt para segurança das senhas.

#### Modelos de Dados (Pydantic)
- `Endereco`: Dados de endereço completo (rua, número, complemento, bairro, cidade, estado, cep)
- `CadastroUsuario`: Dados completos do usuário incluindo endereço
- `LoginUsuario`: Credenciais de login (email e senha)
- `Livro`: Informações básicas do livro (id, título, autor)
- `Pedido`: Dados do pedido (id_pedido, id_usuario)
- `CalculoFrete`: Dados para cálculo de frete (CEP)

#### Segurança
- **Hash de Senhas**: Utiliza MD5 com salt "salt_de_teste" para proteger senhas
- **Geração de IDs**: UUIDs únicos para usuários e pedidos
- **Validação**: Integração com módulo de validação para emails e senhas

#### Endpoints Disponíveis

##### Usuários
- `POST /v1/usuario/cadastrar/`: Cadastro de novo usuário com validação completa
- `POST /v1/usuario/logar/`: Login de usuário com hash MD5+salt

##### Biblioteca
- `GET /v1/livros/`: Lista todos os livros disponíveis (literatura LGBTQ+)

##### Carrinho
- `POST /v1/loja/carrinho/adicionar/{idLivro}`: Adiciona livro ao carrinho
- `DELETE /v1/loja/carrinho/remover/{idLivro}`: Remove livro do carrinho

##### Pedidos
- `GET /v1/loja/pedido/criar/`: Cria um novo pedido a partir do carrinho atual
- `POST /v1/loja/pedido/confirmar/{idPedido}`: Confirma um pedido existente
- `DELETE /v1/loja/pedido/cancelar/{idPedido}`: Cancela um pedido existente

### 2. Lógica de Negócio e Mock Data (requisicao.py)

Este módulo contém a lógica de negócio e dados de demonstração (mock data) para o sistema.

#### Mock Data (Dados de Demonstração)
- `mock_usuarios`: Dicionário de usuários cadastrados
- `mock_livros`: Lista de 6 livros de literatura LGBTQ+ pré-carregados
- `mock_carrinho`: Dicionário de carrinhos por usuário
- `mock_pedidos`: Dicionário de pedidos criados

#### Catálogo de Livros
O sistema inclui livros focados em literatura LGBTQ+:
1. "Red: A História de Chapeuzinho Vermelho" - Liesl Shurtliff
2. "Cemitério" - João Silvério Trevisan  
3. "O Menino do Pijama Listrado Arco-Íris" - Alex Gino
4. "Giovanni's Room" - James Baldwin
5. "Aristóteles e Dante Descobrem os Segredos do Universo" - Benjamin Alire Sáenz
6. "A Miseducação de Cameron Post" - Emily M. Danforth

#### Classes
1. `Endpoints`
   - Gerencia URLs dos endpoints da API externa
   - Métodos para construir URLs para cada operação

2. `Requisicao`
   - Implementa a lógica de negócio usando mock data
   - Métodos principais:
     - `cadastrar()`: Cadastro de usuário com verificação de duplicidade
     - `logar()`: Login com validação de credenciais
     - `listar_biblioteca()`: Retorna catálogo de livros
     - `adicionar_no_carrinho()`: Gerencia adição de itens
     - `remover_do_carrinho()`: Gerencia remoção de itens
     - `criar_pedido()`: Converte carrinho em pedido com cálculo de preço
     - `confirmar_pedido()`: Finaliza pedido e limpa carrinho
     - `cancelar_pedido()`: Cancela pedido e restaura carrinho

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
   pip install fastapi uvicorn requests email-validator pydantic
   ```

### Executando o Servidor

1. Inicie o servidor FastAPI:
   ```bash
   uvicorn backend.api.integracao_front:app --reload --port 8000
   ```

2. O servidor estará disponível em `http://localhost:8000`
3. Documentação interativa disponível em `http://localhost:8000/docs`

### Executando os Testes

```bash
# Teste de integração completo
python teste_integracao.py

# Testes específicos da API
python teste-backend-api-requisicao.py
```

## Fluxo de Operações

1. **Cadastro**: Usuário se cadastra com dados completos e endereço
2. **Login**: Sistema valida credenciais com hash MD5+salt
3. **Navegação**: Usuário visualiza catálogo de livros LGBTQ+
4. **Carrinho**: Adiciona/remove livros do carrinho pessoal
5. **Pedido**: Cria pedido a partir do carrinho (com taxa de entrega R$ 5,40)
6. **Finalização**: Confirma ou cancela o pedido

## Observações Técnicas

- **Mock Data**: Sistema usa dados simulados para demonstração
- **Segurança**: Implementa hash MD5 com salt para senhas (para produção, use bcrypt)
- **IDs Únicos**: Utiliza UUID4 para usuários e UUID1 para pedidos
- **Validações**: Validação robusta de emails, senhas e dados de endereço
- **API REST**: Segue padrões REST com códigos de status HTTP apropriados
- **Tratamento de Erros**: Retorna mensagens de erro detalhadas para debugging
- **Literatura Especializada**: Foco em livros de literatura LGBTQ+ e diversidade
