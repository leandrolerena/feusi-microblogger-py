from datetime import datetime
from app.model.post import Post
from app.model.user import User


def test_post_str_representation():
    """Test that Post string representation includes content and username."""
    test_user = User(name="test_user")
    test_post = Post(
        content="Hello world",
        user=test_user,
        timestamp=datetime(2025, 1, 1, 12, 0, 0),
    )
    result = str(test_post)
    assert "Hello world" in result
    assert "test_user" in result
    assert "2025-01-01 12:00:00" in result
