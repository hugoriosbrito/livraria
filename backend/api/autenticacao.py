from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer

CHAVE_SECRETA = "livrariaarcoiris"
ALGORITMO = "HS256"

security = HTTPBearer()
class AutenticacaoJWT:

    @staticmethod
    def criar_token(user_data: dict): #criacao do token
        dados = {
            "user_id": user_data["id_usuario"],
            "email": user_data["email"],
            "nome": user_data["nome"],
            "exp": datetime.now(timezone.utc) + timedelta(hours=24)  #token expira em 24 horas
        }
        token = jwt.encode(dados, CHAVE_SECRETA, algorithm=ALGORITMO)
        return token

    @staticmethod
    def verificar_token(credentials = Depends(security)): #verifica a validade do token
        token = credentials.credentials
        
        try:
            payload = jwt.decode(token, CHAVE_SECRETA, algorithms=[ALGORITMO])
            return payload
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido ou expirado!"
            )