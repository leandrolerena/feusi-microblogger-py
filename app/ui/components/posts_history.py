import streamlit as st

from app.persistence import storage


def show_posts_history():
    all_posts = storage.get_posts()
    st.subheader("Posts")
    for i, post in enumerate(all_posts):
        st.write(f"{i}. - {str(post)}")
