# This Docker container configuration is only used if it is not possible
# to run this sample Python app on your own environment. For example, you
# either don't have a Python runtime environment or you can't install one.

# Use the same docker image as the one specified in gitlab-ci.yml.
FROM 192.168.1.37:5000/cdpf-python:3.5

# Set the working directory inside the Docker image
WORKDIR /sample-ci-python

# Copy everything
COPY . /sample-ci-python

# Install dependencies
RUN pip3 install -r requirements.txt

# Install the app (using setup.py)
RUN pip3 install -e .
