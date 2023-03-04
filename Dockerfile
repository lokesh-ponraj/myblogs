FROM python:3

RUN pip install pipenv

ENV PROJECT_DIR /usr/local/bin/blogs/blogs

WORKDIR ${PROJECT_DIR}

COPY Pipfile Pipfile.lock ${PROJECT_DIR}/

RUN pipenv install --system --deploy

