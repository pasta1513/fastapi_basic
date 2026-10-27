from schemas.user_schemas import User

users : list[User] = [
    User(username = 'aaa',
         password = '111',
         email = 'aaa@aaa.com',
         name = 'AAA'),
    User(username = 'bbb',
         password = '222',
         email = 'bbb@bbb.com',
         name = 'BBB'),
]

async def select_users() -> list[User]:
    return users

async def select_user(email: str) -> User | None:
    # print('email 데이터베이스 연결: ', email)
    for user in users:
        # print(user)
        if user.email == email:
            return user
        
    return None

async def insert(user: User) -> User | None:
    # print('insert user: ', user)
    for u in users:
        if u.email == user.email:
            return None
        
    users.append(user)
    return user

async def update(username: str, user: User):
    for i, u in enumerate(users):
        if u.username == username:
            users[i] = user
            return u

    return None

async def delete(username: str):
    for i, u in enumerate(users):
        if u.username == username:
            delete_user = users.pop(i)
            return delete_user

    return None