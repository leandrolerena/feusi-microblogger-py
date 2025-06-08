import streamlit as st
from app.model.post import Post
from app.persistence.storage import storage


def show_add_new_post():
    st.subheader("Add a new post")

    # Get current user name from session state
    user_name = st.session_state.user_name if "user_name" in st.session_state else ""

    new_post = st.text_input("Write a new post", key="new_post_input")
    if st.button("Submit", key="submit_button"):
        if new_post.strip():
            # Create post with content and user name
            storage.add_post(Post(content=new_post.strip(), user_name=user_name))
            st.rerun()
