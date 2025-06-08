"""
This script is the entry point for the Streamlit application.
It calls the Streamlit bootstrap function to run the app.
"""
import inspect
import app.streamlit_app

import streamlit.web.bootstrap

file_path = inspect.getfile(app.streamlit_app)

def main():
    streamlit.web.bootstrap.run(
        file_path,
        False,  # Command-line args as a string, e.g. "--server.port 8502"
        [],
        {},
    )

if __name__ == "__main__":
    main()
