import unittest
from backend.api.requisicao import Requisicao, Endpoints

BASE_URL = 'http://localhost:8000/api'
idLivro = 5
idPedido = 2

get_cadastro_endpoint = f'{BASE_URL}/v1/cadastrar/'
get_logar_endpoint = f'{BASE_URL}/v1/login/'
get_biblioteca_listar_endpoint = f'{BASE_URL}/v1/biblioteca/listar/'
get_carrinho_adicionar_endpoint = f'{BASE_URL}/v1/carrinho/adicionar/{idLivro}'
get_carrinho_remover_endpoint = f'{BASE_URL}/v1/carrinho/remover/{idLivro}'
get_pedido_confirmar_endpoint = f'{BASE_URL}/v1/pedido/confirmar/{idPedido}'
get_pedido_cancelar_endpoint = f'{BASE_URL}/v1/pedido/cancelar/{idPedido}'

end = Endpoints(url_base=BASE_URL)
req = Requisicao(end)

class CasoTesteReqAPI(unittest.TestCase):
    def test_requisicao_cadastrar(self):
        retorno_cadastro = req.cadastrar({"nome": "Hugo", "sobrenome": "Rios",
                                          "email": "email", "senha": "senha"})
        self.assertEqual(retorno_cadastro.status_code, 201)

    def test_requisicao_logar(self):
        retorno_logar = req.logar({"email": "email", "senha": "senha"})
        self.assertEqual(retorno_logar.status_code, 200)

    def test_requisicao_listar_biblioteca(self):
        retorno_biblioteca = req.listar_biblioteca()
        self.assertEqual(retorno_biblioteca.status_code, 200)
        self.assertIsInstance(retorno_biblioteca.json(), list)

    def test_requisicao_adicionar_carrinho(self):
        retorno_adicionar = req.adicionar_no_carrinho(idLivro)
        self.assertEqual(retorno_adicionar.status_code, 200)

    def test_requisicao_remover_carrinho(self):
        retorno_remover = req.remover_do_carrinho(idLivro)
        self.assertEqual(retorno_remover.status_code, 200)

    def test_requisicao_confirmar_pedido(self):
        retorno_confirmar_pedido = req.confirmar_pedido(idPedido)
        self.assertEqual(retorno_confirmar_pedido.status_code, 200)

    def test_requisicao_cancelar_pedido(self):
        retorno_cancelar_pedido = req.cancelar_pedido(idPedido)
        self.assertEqual(retorno_cancelar_pedido.status_code, 200)

    def test_cadastro_endpoint(self):
        self.assertEqual(get_cadastro_endpoint, f'{BASE_URL}/v1/cadastrar/')

    def test_login_endpoint(self):
        self.assertEqual(get_logar_endpoint, f'{BASE_URL}/v1/login/')

    def test_biblioteca_listar_endpoint(self):
        self.assertEqual(get_biblioteca_listar_endpoint, f'{BASE_URL}/v1/biblioteca/listar/')

    def test_carrinho_adicionar_endpoint(self):
        self.assertEqual(get_carrinho_adicionar_endpoint, f'{BASE_URL}/v1/carrinho/adicionar/{idLivro}')

    def test_carrinho_remover_endpoint(self):
        self.assertEqual(get_carrinho_remover_endpoint, f'{BASE_URL}/v1/carrinho/remover/{idLivro}')

    def test_pedido_confirmar_endpoint(self):
        self.assertEqual(get_pedido_confirmar_endpoint, f'{BASE_URL}/v1/pedido/confirmar/{idPedido}')

    def test_pedido_cancelar_endpoint(self):
        self.assertEqual(get_pedido_cancelar_endpoint, f'{BASE_URL}/v1/pedido/cancelar/{idPedido}')

if __name__ == '__main__':
    unittest.main()
