import requests
from datetime import datetime
#REQUISIÇÕES PARA API DO BACKEND JAVA QUE VAI RETORNAR OS DADOS DO BANCO DE DADOS

mock_usuarios = {}
mock_livros = [
{
                "idLivro": 1,
                "nomeLivro": "Red: A História de Chapeuzinho Vermelho",
                "autor": "Liesl Shurtliff",
                "descricao": "Uma releitura moderna do clássico conto, explorando temas de identidade e aceitação",
                "preco": 29.90,
                "urlImagem": "https://picsum.photos/200",
                "quantidadeEstoque": 15,
                "generoLivro": "Literatura Juvenil LGBTQ+"
            },
            {
                "idLivro": 2, 
                "nomeLivro": "Cemitério",
                "autor": "João Silvério Trevisan",
                "descricao": "Romance brasileiro que aborda a experiência gay na ditadura militar",
                "preco": 34.50,
                "urlImagem": "https://picsum.photos/200",
                "quantidadeEstoque": 8,
                "generoLivro": "Literatura Brasileira LGBTQ+"
            },
            {
                "idLivro": 3,
                "nomeLivro": "O Menino do Pijama Listrado Arco-Íris",
                "autor": "Alex Gino",
                "descricao": "História tocante sobre uma criança transgênero e sua jornada de autodescoberta",
                "preco": 28.90,
                "urlImagem": "https://picsum.photos/200",
                "quantidadeEstoque": 0,
                "generoLivro": "Literatura Infanto-Juvenil Trans"
            },
            {
                "idLivro": 4,
                "nomeLivro": "Giovanni's Room",
                "autor": "James Baldwin",
                "descricao": "Clássico da literatura LGBTQ+ que explora amor, identidade e aceitação",
                "preco": 32.00,
                "urlImagem": "https://picsum.photos/200",
                "quantidadeEstoque": 12,
                "generoLivro": "Literatura Clássica LGBTQ+"
            },
            {
                "idLivro": 5,
                "nomeLivro": "Aristoteles e Dante Descobrem os Segredos do Universo",
                "autor": "Benjamin Alire Sáenz",
                "descricao": "Romance sobre dois adolescentes mexicano-americanos que descobrem o amor",
                "preco": 36.90,
                "urlImagem": "https://picsum.photos/200",
                "quantidadeEstoque": 20,
                "generoLivro": "Romance Young Adult LGBTQ+"
            },
            {
                "idLivro": 6,
                "nomeLivro": "A Miseducação de Cameron Post",
                "autor": "Emily M. Danforth",
                "descricao": "História sobre uma adolescente lésbica em um campo de 'terapia de conversão'",
                "preco": 31.50,
                "urlImagem": "https://picsum.photos/200",
                "quantidadeEstoque": 6,
                "generoLivro": "Drama LGBTQ+"
            }
]
mock_carrinho = {}
mock_pedidos = {}


class Endpoints:
    def __init__(self, url_base):
        self.url_base = url_base

    def get_cadastro_endpoint(self):
        return f"{self.url_base}/v1/cadastrar/"

    def get_logar_endpoint(self):
        return f"{self.url_base}/v1/login/"

    def get_biblioteca_listar_endpoint(self):
        return f"{self.url_base}/v1/biblioteca/listar/"

    def get_carrinho_adicionar_endpoint(self, idLivro):
        return f"{self.url_base}/v1/carrinho/adicionar/{idLivro}"

    def get_carrinho_remover_endpoint(self, idLivro):
        return f"{self.url_base}/v1/carrinho/remover/{idLivro}"

    def get_pedido_confirmar_endpoint(self, idPedido):
        return f"{self.url_base}/v1/pedido/confirmar/{idPedido}"

    def get_pedido_cancelar_endpoint(self, idPedido):
        return f"{self.url_base}/v1/pedido/cancelar/{idPedido}"

class Requisicao:

    def __init__(self, endpoints: Endpoints):
        self.endpoints = endpoints

    def enviar_requisicao(self, metodo, url, data=None):
        if metodo == "GET":
            return requests.get(url)
        elif metodo == "POST":
            return requests.post(url, data)
        elif metodo == "DELETE":
            return requests.delete(url)
        raise ValueError("Método de requisição inválido! Use 'GET', 'POST' ou 'DELETE'.")

    def listar_biblioteca(self):
        endpoint_url = self.endpoints.get_biblioteca_listar_endpoint()

        return mock_livros
        """      
        return self.enviar_requisicao(
            "GET",
            endpoint_url
        )"""

    def cadastrar(self, data):
        endpoint_url = self.endpoints.get_cadastro_endpoint()

        print(data)
        print(data.get("email"))

        for usuario in mock_usuarios.values():
            if usuario.get("email") == data.get("email"):
                return {"status":"erro","mensagem": "Usuário já cadastrado"}
        
        mock_usuarios[data.get("id_usuario")] = data

        return {"status":"sucesso","mensagem": "Usuário cadastrado com sucesso", "usuario": data}
        
        """
        return self.enviar_requisicao(
            "POST",
            endpoint_url,
            json=data
        )
        """

    def logar(self, data):
        endpoint_url = self.endpoints.get_logar_endpoint()
        
        email_login = data.get("email")
        senha_login = data.get("senha")
        
        for usuario in mock_usuarios.values():
            if usuario.get("email") == email_login:
                if usuario.get("senha") == senha_login:
                    return {"status":"sucesso","mensagem": "Usuário logado com sucesso", "usuario": usuario}
                else:
                    return {"status":"erro","mensagem": "Email ou senha inválidos"}
        
        return {"status":"erro","mensagem": "Email ou senha inválidos"}

        
        """
        return self.enviar_requisicao(
            "POST",
            endpoint_url,
            json=data
        )
        """

    def adicionar_no_carrinho(self, idLivro):
        endpoint_url = self.endpoints.get_carrinho_adicionar_endpoint(idLivro=idLivro)
        
        for livro in mock_livros:
            if livro["idLivro"] == idLivro:
                mock_carrinho[idLivro] = livro
                return {"status":"sucesso", "message": f"Livro {idLivro} adicionado ao carrinho", "livro": livro}

        return {"status":"erro","mensagem": "Livro não encontrado"}
        
        """
        return self.enviar_requisicao(
            "POST",
            endpoint_url,
            json=data
        )
        """

    def remover_do_carrinho(self, idLivro):
        endpoint_url = self.endpoints.get_carrinho_remover_endpoint(idLivro=idLivro)
        
        for livro in mock_livros:
            if idLivro in mock_carrinho:
                livro = mock_carrinho.pop(idLivro)
                return {"message": f"Livro {idLivro} removido do carrinho", "livro": livro}
        return {"status":"erro","mensagem": "Livro não encontrado"}

        """
        return self.enviar_requisicao(
            "DELETE",
            endpoint_url,
        )
        """

    def criar_pedido(self, idPedido):
        endpoint_url = self.endpoints.get_pedido_confirmar_endpoint(idPedido=idPedido)
        
        if not mock_carrinho:
            return {"status": "erro", "mensagem": "Carrinho vazio"}

        itens_pedido = []
        preco_total = 0.0
        
        for idLivro, livro in mock_carrinho.items():
            preco = float(livro["preco"]) if isinstance(livro["preco"], str) else livro["preco"]

            item = {
                "idLivro": str(livro["idLivro"]),
                "nomeLivro": livro["nomeLivro"],
                "quantidade": 1, 
                "preco": f"{preco:.2f}",
                "subtotal": f"{preco:.2f}"
            }
            itens_pedido.append(item)
            preco_total += preco

        taxa_entrega = 5.40
        preco_total += taxa_entrega

        pedido = {
            "status": "pendente",
            "data": {
                "idPedido": idPedido,
                "tipoPedido": "Cartão",  # Cartão, Pix, Boleto
                "precoTotal": f"{preco_total:.2f}",
            },
            "mensagem": "Pedido criado com sucesso"
        }

        mock_pedidos[idPedido] = pedido

        return pedido

    def confirmar_pedido(self, idPedido):
        endpoint_url = self.endpoints.get_pedido_confirmar_endpoint(idPedido=idPedido)
        
        if not mock_carrinho:
            return {"status": "erro", "mensagem": "Carrinho vazio"}

        if idPedido not in mock_pedidos:
            return {"status": "erro", "mensagem": "Pedido não encontrado"}

        pedido = mock_pedidos[idPedido]

        pedido["status"] = "confirmado"
        pedido["mensagem"] = "Pedido confirmado com sucesso"

        mock_carrinho.clear()

        return pedido
        
        """
        return self.enviar_requisicao(
            "POST",
            endpoint_url,
            json=data
        )
        """

    def cancelar_pedido(self, idPedido):
        endpoint_url = self.endpoints.get_pedido_cancelar_endpoint(idPedido=idPedido)
        
        if idPedido not in mock_pedidos:
            return {"status": "erro", "mensagem": "Pedido não encontrado"}

        pedido = mock_pedidos[idPedido]

        pedido["status"] = "cancelado"
        pedido["mensagem"] = "Pedido cancelado com sucesso"

        mock_pedidos.pop(idPedido)
        mock_carrinho.clear()

        return pedido
        
        
        """
        return self.enviar_requisicao(
            "DELETE",
            endpoint_url,
        )
        """