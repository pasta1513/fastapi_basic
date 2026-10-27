from schemas.user_schema import User
# select, insert, update, delete

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