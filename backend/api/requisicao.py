import requests
#REQUISIÇÕES PARA API DO BACKEND JAVA QUE VAI RETORNAR OS DADOS DO BANCO DE DADOS

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
        return self.enviar_requisicao(
            "GET",
            endpoint_url
        )

    def cadastrar(self, data):
        endpoint_url = self.endpoints.get_cadastro_endpoint()
        return self.enviar_requisicao(
            "POST",
            endpoint_url,
            data
        )

    def logar(self, data):
        endpoint_url = self.endpoints.get_logar_endpoint()
        return self.enviar_requisicao(
            "POST",
            endpoint_url,
            data
        )

    def adicionar_no_carrinho(self, data):
        endpoint_url = self.endpoints.get_carrinho_adicionar_endpoint(idLivro=data["idLivro"])
        return self.enviar_requisicao(
            "POST",
            endpoint_url,
            data
        )

    def remover_do_carrinho(self, data):
        endpoint_url = self.endpoints.get_carrinho_remover_endpoint(idLivro=data["idLivro"])
        return self.enviar_requisicao(
            "DELETE",
            endpoint_url,
        )

    def confirmar_pedido(self, data):
        endpoint_url = self.endpoints.get_pedido_confirmar_endpoint(idPedido=data["idPedido"])
        return self.enviar_requisicao(
            "POST",
            endpoint_url,
        )


    def cancelar_pedido(self, data):
        endpoint_url = self.endpoints.get_pedido_cancelar_endpoint(idPedido=data["idPedido"])
        return self.enviar_requisicao(
            "DELETE",
            endpoint_url,
        )

