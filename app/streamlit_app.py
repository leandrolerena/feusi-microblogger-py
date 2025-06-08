import streamlit as st
from streamlit_autorefresh import st_autorefresh

from app.ui.components.add_new_post import show_add_new_post
from app.ui.components.posts_history import show_posts_history
from app.ui.components.configure_user_name import show_configure_user_name

st.title("Microblogger")

# Show user configuration
show_configure_user_name()

# Show other components
show_posts_history()
show_add_new_post()

st_autorefresh(interval=2000, limit=None, key="auto-refresh")
