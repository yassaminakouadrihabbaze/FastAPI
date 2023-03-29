FROM python:3.11

WORKDIR /app

COPY Pipfile Pipfile.lock /app/

RUN pip install pipenv && \
    pipenv install --system --deploy --ignore-pipfile

COPY . /app/

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
