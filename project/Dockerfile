################################################################################
# Stage 1: Run all installation and copy assets
################################################################################
FROM python:3.10.1-slim-buster as installer

# Set working directory
RUN mkdir /build
RUN mkdir /build/app

WORKDIR /build

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc g++ postgresql \
    tree sudo nano \
  && apt-get clean

RUN pip install --upgrade pip
COPY reqs/requirements-app.txt /build/
RUN pip install -r /build/requirements-app.txt

COPY api /build/app/api

# ################################################################################
# # Stage 2: Run the tests in the container.
# ################################################################################
FROM installer as tester

WORKDIR /build

# We want the ability to skip tests completely if desired
ARG skip_tests=1

COPY pytest.ini /build/
COPY tests /build/tests
COPY reqs/requirements-test.txt /build/

# Only run installation of test dependencies if we want to run tests
RUN \
    if [ "$skip_tests" = "" ] ; \
    then \
        pip install -r /build/requirements-test.txt \
            --no-cache-dir \
    else \
        echo "Skipping installation of test dependencies" ; \
    fi

################################################################################
# Stage 3: Build the actual Docker image for the application
################################################################################
FROM installer as api
ENV PYTHONPATH /app

# # Copy the tested code from tester.
COPY --from=installer /build/app /app/
RUN rm -rf /build 

WORKDIR /app
COPY entrypoints/entrypoint.sh ./entrypoint.sh

# Expose the port
EXPOSE ${API_PORT}

# Mount for local development
VOLUME /app/api/

# Run the servers
RUN ["chmod", "+x", "/app/entrypoint.sh"]
CMD ["/app/entrypoint.sh"]
