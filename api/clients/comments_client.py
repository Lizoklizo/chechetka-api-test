from api.clients.base_client import BaseClient


class CommentsClient(BaseClient):
    def get_comments(self, params=None):
        return self.get("/comments", params=params)

    def get_comment_by_id(self, comment_id: int):
        return self.get(f"/comments/{comment_id}")

    def create_comment(self, payload: dict):
        return self.post("/comments", json_body=payload)

    def update_comment(self, comment_id: int, payload: dict):
        return self.put(f"/comments/{comment_id}", json_body=payload)

    def patch_comment(self, comment_id: int, payload: dict):
        return self.patch(f"/comments/{comment_id}", json_body=payload)

    def delete_comment(self, comment_id: int):
        return self.delete(f"/comments/{comment_id}")