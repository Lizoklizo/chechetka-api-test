from api.clients.todos_client import TodosClient


class TodosService:
    def __init__(self, client: TodosClient):
        self.client = client

    def get_all_todos(self, params=None):
        return self.client.get_todos(params=params)

    def get_todo(self, todo_id: int):
        return self.client.get_todo_by_id(todo_id)

    def search_todo(self, query: str):
        return self.client.search_todos(query)

    def create_todo(self, payload: dict):
        return self.client.create_todo(payload)

    def replace_todo(self, todo_id: int, payload: dict):
        return self.client.update_todo(todo_id, payload)

    def update_todo(self, todo_id: int, payload: dict):
        return self.client.patch_todo(todo_id, payload)

    def delete_todo(self, todo_id: int):
        return self.client.delete_todo(todo_id)