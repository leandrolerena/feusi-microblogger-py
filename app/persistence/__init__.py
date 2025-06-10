# Global singleton instance
from .in_memory_post_storage import InMemoryPostStorage
from .post_storage import PostStorage

storage: PostStorage = InMemoryPostStorage()
