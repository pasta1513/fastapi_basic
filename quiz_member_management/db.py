from schemas.user_schema import User
from pydantic import EmailStr

users: list[User] = []

async def select_users() -> list[User]:
    return users

async def select_user(id: str) -> User | None:
    for u in users:
        if u.user_id == id:
            return u

    return None

async def insert_user(user: User) -> User | None:
    for u in users:
        if u.user_id == user.user_id:
            return None

    users.append(user)
    return user

async def update_user(id: str, user: User) -> tuple[User | None, str | None]:
    for i, u in enumerate(users):
        if u.user_id == id:
            for other in users:
                if other.user_id == user.user_id and other.user_id != id:
                    return None, "duplicate"
            
            users[i] = user
            return user, None

    return None, "not_found"

async def delete_user(id: str) -> User | None:
    for i, u in enumerate(users):
        if u.user_id == id:
            new_users = users.pop(i)
            return new_users

    return None

async def sign_in(email: EmailStr, pw: str) -> tuple[User | None, str | None]:
    for u in users:
        if u.user_email == email:
            if u.user_pw == pw:
                return u, None

            return None, "wrong_pw"

        return None, "wrong_email"