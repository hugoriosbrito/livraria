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


