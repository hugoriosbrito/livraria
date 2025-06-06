import requests
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

    def get_download_livro_endpoint(self, idLivro):
        return f"{self.url_base}/v1/livro/download/{idLivro}"

class Requisicao:

    def __init__(self, endpoints: Endpoints):
        self.endpoints = endpoints

    def enviar_requisicao(self, metodo, url, data=None):
        if metodo == "GET":
            return requests.get(url)
        elif metodo == "POST":
            return requests.post(url, data)
        raise ValueError("Método de requisição inválido! Use 'GET', 'POST'")

    def listar_biblioteca(self):
        endpoint_url = self.endpoints.get_biblioteca_listar_endpoint()

        return self.enviar_requisicao(
            "GET",
            endpoint_url
        )

    def cadastrar(self, data):
        endpoint_url = self.endpoints.get_cadastro_endpoint()

        return self.enviar_requisicao(
            "POST",
            endpoint_url,
            data=data
        )


    def logar(self, data):
        endpoint_url = self.endpoints.get_logar_endpoint()

        return self.enviar_requisicao(
            "POST",
            endpoint_url,
            data=data
        )

    def realizar_download(self, idLivro):
        endpoint_url = self.endpoints.get_download_livro_endpoint(idLivro)
