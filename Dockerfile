FROM python:3.10-alpine

WORKDIR /collector-api/

COPY /src /collector-api/src
COPY pyproject.toml pyproject.toml
COPY .env .env

RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

ENTRYPOINT ["python3"]
CMD ["src/main.py"]