from api.clients.base_client import BaseClient


class UsersClient(BaseClient):
    def get_users(self, params=None):
        return self.get("/users", params=params)

    def get_user_by_id(self, user_id: int):
        return self.get(f"/users/{user_id}")

    def search_users(self, query: str):
        return self.get("/users/search", params={"q": query})

    def create_user(self, payload: dict):
        return self.post("/users", json_body=payload)

    def update_user(self, user_id: int, payload: dict):
        return self.put(f"/users/{user_id}", json_body=payload)

    def patch_user(self, user_id: int, payload: dict):
        return self.patch(f"/users/{user_id}", json_body=payload)

    def delete_user(self, user_id: int):
        return self.delete(f"/users/{user_id}")