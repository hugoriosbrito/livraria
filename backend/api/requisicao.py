import requests
#REQUISIÇÕES PARA API DO BACKEND JAVA QUE VAI RETORNAR OS DADOS DO BANCO DE DADOS

class Endpoints:
    def __init__(self, url_base):
        self.url_base = url_base

    def get_cadastro_endpoint(self):
        return f"{self.url_base}/v1/cadastrar"

    def get_logar_endpoint(self):
        return f"{self.url_base}/v1/logar"

    def get_biblioteca_listar_endpoint(self):
        return f"{self.url_base}/v1/livro/listar"

    def get_download_livro_endpoint(self, idLivro):
        return f"{self.url_base}/v1/livro/download/{idLivro}"

class Requisicao:

    def __init__(self, endpoints: Endpoints):
        self.endpoints = endpoints

    def listar_biblioteca(self):
        endpoint_url = self.endpoints.get_biblioteca_listar_endpoint()
        return requests.get(endpoint_url).text

    def cadastrar(self, data):
        endpoint_url = self.endpoints.get_cadastro_endpoint()
        return requests.post(endpoint_url, json=data).text

    def logar(self, data):
        endpoint_url = self.endpoints.get_logar_endpoint()
        return requests.post(endpoint_url, json=data).text

    def realizar_download(self, idLivro, idUsuario):
        endpoint_url = self.endpoints.get_download_livro_endpoint(idLivro)
        return requests.get(endpoint_url, params={"idUsuario": idUsuario}).text
