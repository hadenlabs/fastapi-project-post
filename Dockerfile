#
# Dockerfile for fastapi-project-post
#

FROM python:3.9.2 as base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

WORKDIR /usr/src/app

ENV BASE_DEPS \
    software-properties-common \
    vim \
    bash \
    curl \
    tzdata \
    ca-certificates

ENV PACKAGE_DEPS \
    build-essential \
    libpq-dev \
    git \
    curl \
    gettext

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends ${BASE_DEPS} ${PACKAGE_DEPS} \
    && pip install --no-cache-dir --upgrade pip \
    && mkdir -p logs \
    && apt-get clean \
    && apt-get purge -y \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


FROM base AS python-deps

ENV PIPENV_VENV_IN_PROJECT=${PIPENV_VENV_IN_PROJECT:-1} \
    WORKON_HOME=${WORKON_HOME:-/project/.venv}

WORKDIR /project

ENV MODULES_PYTHON \
    poetry

# Install python dependencies in /project/.venv
COPY Pipfile .

RUN pip install --no-cache --no-cache-dir ${MODULES_PYTHON} \
    && poetry install --dev --skip-lock


FROM base AS runtime

ENV PATH="/project/.venv/bin:${PATH}"

WORKDIR /usr/src/app

COPY . .

COPY --from=python-deps /project/.venv /project/.venv

# Port to expose
EXPOSE 3000

CMD ["python", "main.py"]
