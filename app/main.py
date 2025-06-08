"""
This script is the entry point for the Streamlit application.
It calls the Streamlit bootstrap function to run the app.
"""

import streamlit.web.bootstrap

APP_PATH = "streamlit_app.py"

if __name__ == "__main__":
    streamlit.web.bootstrap.run(
        APP_PATH,
        False,  # Command-line args as a string, e.g. "--server.port 8502"
        [],
        {},
    )
