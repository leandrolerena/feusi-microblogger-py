import streamlit as st

from model.user import User


def show_configure_user_name():
    st.subheader("User Configuration")

    if "user" not in st.session_state:
        st.session_state.user = None

    if st.session_state.user:
        st.write(f"Current user: **{st.session_state.user}**")
        if st.button("Change user name"):
            st.session_state.user = None
    else:
        new_name = st.text_input("Enter your user name", key="user_name_input")
        if st.button("Save user name", key="save_user_name"):
            if new_name.strip():
                st.session_state.user = User(name=new_name.strip())
            else:
                st.warning("Please enter a valid user name")
