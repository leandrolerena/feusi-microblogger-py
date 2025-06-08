from dataclasses import dataclass
from datetime import datetime


@dataclass
class Post:
    content: str
    user_name: str
    timestamp: datetime = datetime.now()

    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}: {self.content} (by {self.user_name})"
