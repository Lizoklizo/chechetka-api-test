from api.clients.posts_client import PostsClient


class PostsService:
    def __init__(self, client: PostsClient):
        self.client = client

    def get_all_posts(self, params=None):
        return self.client.get_posts(params=params)

    def get_post(self, post_id: int):
        return self.client.get_post_by_id(post_id)

    def search_post(self, query: str):
        return self.client.search_posts(query)

    def create_post(self, payload: dict):
        return self.client.create_post(payload)

    def replace_post(self, post_id: int, payload: dict):
        return self.client.update_post(post_id, payload)

    def update_post(self, post_id: int, payload: dict):
        return self.client.patch_post(post_id, payload)

    def delete_post(self, post_id: int):
        return self.client.delete_post(post_id)

    def get_post_likes(self, post_id: int):
        return self.client.get(f"/posts/{post_id}/likes")

    def add_post_like(self, post_id: int, user_id: int = None):
        payload = {"userId": user_id} if user_id else {}
        return self.client.post(f"/posts/{post_id}/likes", json_body=payload)