import streamlit as st

from app.persistence import storage


def show_posts_history():
    all_posts = storage.get_posts()
    st.subheader("Posts")
    for i, post in enumerate(all_posts):
        timestamp_str = post.timestamp.strftime("%Y-%m-%d %H:%M:%S")
        st.write(f"{i+1}. - {str(post)}")
