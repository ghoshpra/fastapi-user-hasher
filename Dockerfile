FROM python:3.10-alpine

WORKDIR /src

ADD user-hasher user-hasher
ADD requirements requirements

ENV ENVIRONMENT prod

RUN pip install --upgrade pip wheel setuptools -r requirements/requirements-prod.txt

ENTRYPOINT ["uvicorn", "user-hasher.main:app", "--host", "0.0.0.0", "--port=8000"]
