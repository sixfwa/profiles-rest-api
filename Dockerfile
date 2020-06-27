# Image that is going to be inherited
FROM python:3.7-alpine
LABEL Francis Ali

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# Creates empty folder called app
RUN mkdir /app
# Switches to /app as the default directory
WORKDIR /app
# Copies from this local machine to the app folder in image
COPY ./app /app

# Create a user called "user"
RUN adduser -D user
# Switch to the user
USER user