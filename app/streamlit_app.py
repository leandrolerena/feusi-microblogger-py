"""
This is the Streamlit application for the Microblogger project.
This file is rendered every time the user accesses the app or interacts with it.
"""

import streamlit as st
from streamlit_autorefresh import st_autorefresh

from app.ui.components.add_new_post import show_add_new_post
from app.ui.components.posts_history import show_posts_history
from app.ui.components.configure_user_name import show_configure_user_name

def main():
    """Main function to run the Streamlit app."""
    # Creates and renders the title of the app
    st.title("Microblogger")

    # Creates and renders a user configuration component
    show_configure_user_name()

    # Creates and renders the post history
    show_posts_history()

    # Creates and renders a component to add a new post
    show_add_new_post()

    # This makes sure the app refreshes every 2 seconds to show newly added posts
    st_autorefresh(interval=2000, limit=None, key="auto-refresh")

if __name__ == "__main__":
    main()
