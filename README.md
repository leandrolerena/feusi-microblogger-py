# Microblogger

The migroblogger is a simple microblogging platform that allows users to post short messages and view a timeline of posts. 
It is built using Python and Streamlit, with an in-memory data store for simplicity. 

For students, it serves as a practical example of a web application which can be extended with more features like user authentication, message deletion, and more.

## Open the application

Open a Terminal or PowerShell window and execute the following command.

```bash
git clone https://github.com/leandrolerena/feusi-microblogger-py.git
cd feusi-microblogger-py
code .
```

if you forked the project, then

```bash
git clone https://github.com/YOUR_USERNAME/feusi-microblogger-py.git
cd feusi-microblogger-py
code .
```


## Install and run the project

To install the project dependencies and run the application, follow these steps (make sure poetry is installed and in your PATH):

```bash
poetry install
poetry run app
```

## Run static code analysis (Pylint)

To run Pylint on the project, use the following command:

```bash
 poetry run pylint ./app
```

# Run automatic tests (Pytest)

To run the tests using Pytest, use the following command:

```bash
poetry run pytest
```

# Run the code formatter (Black)

To format the code using Black, use the following command:

```bash
poetry run black ./app
```