from api.clients.users_client import UsersClient


class UsersService:
    def __init__(self, users_client: UsersClient):
        self.users_client = users_client

    def get_all_users(self):
        return self.users_client.get_users()

    def get_user(self, user_id: int):
        return self.users_client.get_user_by_id(user_id)

    def search_user(self, query: str):
        return self.users_client.search_users(query)

    def create_user(self, payload: dict):
        return self.users_client.create_user(payload)

    def replace_user(self, user_id: int, payload: dict):
        return self.users_client.update_user(user_id, payload)

    def update_user_partially(self, user_id: int, payload: dict):
        return self.users_client.patch_user(user_id, payload)

    def remove_user(self, user_id: int):
        return self.users_client.delete_user(user_id)