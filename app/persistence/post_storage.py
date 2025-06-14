from abc import abstractmethod

from app.model.post import Post


class PostStorage:
    @abstractmethod
    def add_post(self, post: Post):
        """Add a post to the storage."""

    @abstractmethod
    def get_posts(self):
        """Retrieve all posts from the storage."""

    @abstractmethod
    def clear(self):
        """Clear all posts from the storage."""
