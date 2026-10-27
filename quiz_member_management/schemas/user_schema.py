from pydantic import BaseModel, EmailStr

class User(BaseModel):
    user_id: str
    user_pw: str
    user_email: EmailStr
    user_name: str