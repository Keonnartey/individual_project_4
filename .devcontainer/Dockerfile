# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.245.2/containers/codespaces-linux/.devcontainer/base.Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.10.8

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
RUN apt-get update && apt-get -y install --no-install-recommends \
   python3.8-venv \
   gcc 

ARG USER="codespace"
ARG VENV_PATH="/home/${USER}/venv"

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file and the Makefile from /tmp to /app
COPY /tmp/requirements.txt .
COPY /tmp/Makefile .

# Create a virtual environment and install dependencies
RUN python3 -m venv ${VENV_PATH} \
   && ${VENV_PATH}/bin/pip --disable-pip-version-check --no-cache-dir install -r requirements.txt \
   && rm -rf requirements.txt Makefile

# Define environment variable
ENV NAME World

# Copy all the content of the current directory to /app
COPY . .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "app.py", "--host=0.0.0.0", "--port=5000"]
