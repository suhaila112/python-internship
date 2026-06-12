from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class LoginRequest(BaseModel):
    email: str
    password: str


@app.post("/auth/login")
def login(data: LoginRequest):

    # Demo credentials
    if (
        data.email == "zamam@gmail.com"
        and data.password == "123456789"
    ):
        return {
            "token": "abc123"
        }

    raise HTTPException(
        status_code=401,
        detail="Invalid email or password"
    )