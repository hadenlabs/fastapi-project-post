#
# Dockerfile for fastapi-project-post
#

FROM python:3.11.2-slim as base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1
ENV USERNAME appuser
ENV PORT=8000
ENV STAGE=production

WORKDIR /usr/src/app

ENV BASE_DEPS \
    git \
    vim \
    bash \
    curl \
    tzdata \
    ca-certificates

ENV BUILD_DEPS \
    curl \
    libpq-dev \
    build-essential \
    software-properties-common \
    gcc \
    musl-dev \
    libffi-dev \
    gettext \
    openssl \
    autoconf \
    pkgconf \
    python3-cffi \
    libssl-dev \
    libtool

ENV PACKAGES_PIP \
    poetry


FROM base as requirements-stage

WORKDIR /build

COPY ./pyproject.toml ./poetry.lock* /build/

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends ${BUILD_DEPS} \
    && pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir ${PACKAGES_PIP} \
    && poetry config virtualenvs.create false \
    && poetry export --with dev --with test --format requirements.txt --output requirements.txt --without-hashes \
    && apt-get clean \
    && apt-get purge -y \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


FROM base as runtime

WORKDIR /usr/src/app

# Create a non-root user

COPY --from=requirements-stage /build/requirements.txt requirements.txt

COPY . .

RUN apt-get update -y \
  && apt-get install -y --no-install-recommends ${BASE_DEPS} ${BUILD_DEPS} \
  && pip install --no-cache-dir -r requirements.txt \
  && apt-get clean \
  && apt-get purge -y \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 8000

CMD ["python", "main.py"]
