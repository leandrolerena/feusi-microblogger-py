import inspect

from streamlit.testing.v1 import AppTest
import app.streamlit_app
from app.persistence import storage


def test_user_post_flow():
    """Test the complete flow of user entering name and adding a post."""
    # Clear any existing test data
    storage.clear()

    # Create and run the Streamlit app test
    file_path = inspect.getfile(app.streamlit_app)
    print(file_path)
    at = AppTest.from_file(file_path).run()
    
    # Simulate entering username
    at.text_input(key="user_name_input").input("TestUser").run()
    at.button(key="save_user_name").click().run()
    
    # Simulate adding a post
    test_post_content = "This is a test post"
    at.text_input(key="new_post_input").input(test_post_content).run()
    at.button(key="add_post").click().run()
    
    # Verify the post was added
    posts = storage.get_posts()
    assert len(posts) == 1
    assert posts[0].content == test_post_content

