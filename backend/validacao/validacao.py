from datetime import datetime
from email_validator import validate_email, EmailNotValidError

#CLASSE PARA VALIDAÇÃO DE DADOS DO FRONTEND

#caracteres especiais para validação das senhas
CARACTERES_ESPECIAIS = "!@#$%^&*()_+-=[]{}|;:,.<>/?`~\"'´`÷×€£¥¢₹₽₩©®™←↑→↓↔↕↖↗↘↙■□▪▫▲▼◀▶◆◇○●◎★☆♩♪♫♬♭♮♯ÆÐĦĲŁØŒÞẞµ\\"


class ValidacaoException(Exception):
    pass


class Validacao:
    @staticmethod
    def validar_email(email):
        """Valida se o e-mail fornecido é válido e normalizado."""
        try:
            email_normalizado = validate_email(email).normalized
            return bool(email_normalizado)
        except EmailNotValidError as e:
            raise ValidacaoException(f"E-mail inválido: {str(e)}")

    @staticmethod
    def validar_senha(senha):
        """Valida se a senha atende aos requisitos: comprimento e caracteres especiais."""
        if len(senha) < 8:
            raise ValidacaoException("A senha deve ter pelo menos 8 caracteres.")
        if not any(char in senha for char in CARACTERES_ESPECIAIS):
            raise ValidacaoException("A senha deve conter pelo menos um caractere especial.")

    @staticmethod
    def validar_endereco(endereco):
        """Checa se o endereço possui um CEP válido."""
        if 'cep' not in endereco or not endereco['cep']:
            raise ValidacaoException("Endereço inválido: CEP não encontrado.")
        return True

    @staticmethod
    def validar_numero_cartao(numero_cartao: str):
        """Valida o número do cartão, checando se é numérico e tem 13 a 19 dígitos."""
        if not numero_cartao.isdigit():
            raise ValidacaoException("Número do cartão deve conter apenas dígitos.")
        if not 13 <= len(numero_cartao) <= 19:
            raise ValidacaoException("O número do cartão deve ter entre 13 e 19 dígitos.")
        return True

    @staticmethod
    def validar_data_expiracao_cartao(data_expiracao: str):
        """Valida a data de expiração no formato MM/AAAA e verifica se não está expirada."""
        if type(data_expiracao) is not str:
            raise ValidacaoException("Data de expiração deve ser uma string no formato MM/AAAA.")

        try:
            mes, ano = map(int, data_expiracao.split("/"))
        except ValueError:
            raise ValidacaoException("Formato inválido: use MM/AAAA.")

        ano_atual = datetime.now().year
        mes_atual = datetime.now().month

        if ano < ano_atual or (ano == ano_atual and mes < mes_atual):
            raise ValidacaoException("Data de expiração inválida ou retrógrada.")
        return True

    @staticmethod
    def validar_cvv(cvv: str):
        """Valida o CVV, garantindo que tenha exatamente 3 dígitos."""
        if not (len(cvv) == 3 and cvv.isdigit()):
            raise ValidacaoException("O cvv deve conter exatamente 3 dígitos.")
        return True


