from dataclasses import dataclass
from datetime import datetime
from .user import User


@dataclass
class Post:
    """
    Post model representing a post in the application.
    It contains the content of the post, the user who created it, and a timestamp.
    """

    content: str
    user: User
    timestamp: datetime = datetime.now()

    """
    Returns a string representation of the Post object.
    This method is called whenever a Post object is printed or converted to a string.
    e.g. print(post) or str(post).
    """

    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}: {self.content} (by {self.user})"

    def is_valid(self) -> bool:
        """
        Validates the Post object.
        A post is considered valid if it has content and a user.
        """
        has_content = bool(self.content)
        has_user = bool(self.user)
        return has_content and has_user
