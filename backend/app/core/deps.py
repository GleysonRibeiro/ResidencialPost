from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt
from app.core.config import JWT_SECRET, ALGORITHM

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials

    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[ALGORITHM])
        return payload
    except:
        raise HTTPException(status_code=401, detail="Token inválido")


def require_role(required_roles: list):
    def role_checker(user=Depends(get_current_user)):
        if user.get("perfil") not in required_roles:
            raise HTTPException(status_code=403, detail="Acesso negado")
        return user
    return role_checker