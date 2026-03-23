from api.clients.base_client import BaseClient


class PostsClient(BaseClient):
    def get_posts(self, params=None):
        return self.get("/posts", params=params)

    def get_post_by_id(self, post_id: int):
        return self.get(f"/posts/{post_id}")

    def search_posts(self, query: str):
        return self.get("/posts/search", params={"q": query})

    def create_post(self, payload: dict):
        return self.post("/posts", json_body=payload)

    def update_post(self, post_id: int, payload: dict):
        return self.put(f"/posts/{post_id}", json_body=payload)

    def patch_post(self, post_id: int, payload: dict):
        return self.patch(f"/posts/{post_id}", json_body=payload)

    def delete_post(self, post_id: int):
        return self.delete(f"/posts/{post_id}")