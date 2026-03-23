from api.clients.comments_client import CommentsClient


class CommentsService:
    def __init__(self, client: CommentsClient):
        self.client = client

    def get_all_comments(self, params=None):
        return self.client.get_comments(params=params)

    def get_comment(self, comment_id: int):
        return self.client.get_comment_by_id(comment_id)

    def create_comment(self, payload: dict):
        return self.client.create_comment(payload)

    def replace_comment(self, comment_id: int, payload: dict):
        return self.client.update_comment(comment_id, payload)

    def update_comment_partially(self, comment_id: int, payload: dict):
        return self.client.patch_comment(comment_id, payload)

    def remove_comment(self, comment_id: int):
        return self.client.delete_comment(comment_id)