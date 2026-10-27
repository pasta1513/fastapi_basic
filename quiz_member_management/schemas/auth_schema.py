from pydantic import BaseModel, EmailStr

class UserSingIn(BaseModel):
    email: EmailStr
    pw: str 