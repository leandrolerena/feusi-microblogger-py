import threading
from app.model.post import Post


class PostStorage:
    """
    lass to manage posts in a thread-safe manner.
    """

    def __init__(self):
        self.posts: list[Post] = []
        self.posts_lock = threading.Lock()

    def add_post(self, post: Post):
        with self.posts_lock:
            self.posts.append(post)

    def get_posts(self):
        with self.posts_lock:
            return self.posts.copy()

# Global singleton instance
storage = PostStorage()
