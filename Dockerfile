FROM python:3.5

LABEL NAME="python-3.5" \
      VERSION="3.5" \
      DESC="Standard Python 3.5 runtime."

# Set the working directory inside the Docker image
WORKDIR /sample-ci-python

# Copy everything
COPY . /sample-ci-python

# Install dependencies
RUN pip3 install -r requirements.txt

# Install the app (using setup.py)
RUN pip3 install -e .
