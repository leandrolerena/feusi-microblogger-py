FROM python:3.12

WORKDIR /app

RUN pip install poetry

# Install project deps
COPY pyproject.toml .
COPY poetry.lock .

RUN poetry install

COPY . .

RUN poetry install

EXPOSE 8501
CMD ["poetry", "run", "app"]
