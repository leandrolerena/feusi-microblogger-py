import sys
import streamlit.web.bootstrap
app_path = "streamlit_app.py"

if __name__ == '__main__':
    streamlit.web.bootstrap.run(
        app_path,
        False,  # Command-line args as a string, e.g. "--server.port 8502"
        [],
        {}
    )
