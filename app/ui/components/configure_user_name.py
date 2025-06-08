import streamlit as st


def show_configure_user_name():
    st.subheader("User Configuration")

    if "user_name" not in st.session_state:
        st.session_state.user_name = ""

    if st.session_state.user_name:
        st.write(f"Current user: **{st.session_state.user_name}**")
        if st.button("Change user name"):
            st.session_state.user_name = ""
    else:
        new_name = st.text_input("Enter your user name")
        if st.button("Save user name"):
            if new_name.strip():
                st.session_state.user_name = new_name.strip()
            else:
                st.warning("Please enter a valid user name")
