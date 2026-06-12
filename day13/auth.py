import uuid
from fastapi import Header,HTTPException
from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=["bcrypt"]
)

sessions = {}

def hash_password(password):
    return pwd_context.hash(password)

def verify_password(password, hashed):
    return pwd_context.verify(
        password,
        hashed
    )

def create_token():
    return str(uuid.uuid4())

def get_current_user(
        authorization: str = Header(None)
):
    
    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Token missing"
        )
    
    token = authorization.replace(
        "Bearer ",
        ""
    ) 

    if token not in sessions:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )
    
    return sessions[token]
