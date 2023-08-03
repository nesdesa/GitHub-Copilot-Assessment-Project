FROM python:3.11

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /cms_app

# Set the working directory to /cms_app
WORKDIR /cms_app

# Copy the current directory contents into the container at /cms_app
ADD . /cms_app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

