from api.clients.base_client import BaseClient


class TodosClient(BaseClient):
    def get_todos(self, params=None):
        return self.get("/todos", params=params)

    def get_todo_by_id(self, todo_id: int):
        return self.get(f"/todos/{todo_id}")

    def search_todos(self, query: str):
        return self.get("/todos/search", params={"q": query})

    def create_todo(self, payload: dict):
        return self.post("/todos", json_body=payload)

    def update_todo(self, todo_id: int, payload: dict):
        return self.put(f"/todos/{todo_id}", json_body=payload)

    def patch_todo(self, todo_id: int, payload: dict):
        return self.patch(f"/todos/{todo_id}", json_body=payload)

    def delete_todo(self, todo_id: int):
        return self.delete(f"/todos/{todo_id}")