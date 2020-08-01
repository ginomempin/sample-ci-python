FROM python:3.8

LABEL NAME="python-3.8" \
      VERSION="3.8" \
      DESC="Python3.8 container"

# Set the working directory inside the Docker image
WORKDIR /workspace

# Copy everything except for files listed in .dockerignore
COPY . /workspace

# Install dependencies
RUN pip install -r requirements.txt

# Install the app
RUN pip install -e .
