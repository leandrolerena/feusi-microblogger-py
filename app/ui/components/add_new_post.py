import streamlit as st
from app.model.post import Post
from app.persistence import storage


def show_add_new_post():
    st.subheader("Add a new post")

    # Get current user name from session state
    user = st.session_state.user if "user" in st.session_state else None

    new_post = st.text_input("Write a new post", key="new_post_input")
    if st.button("Submit", key="add_post"):
        post = Post(content=new_post.strip(), user=user)
        if post.is_valid():
            # Create post with content and user name
            storage.add_post(post)
        else:
            st.warning("Post content is not valid")
