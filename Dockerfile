# start from base
FROM ubuntu:18.04

LABEL maintainer="Simon <dynamowebdesign@gmail.com>"

# install system-wide deps for python and node
RUN apt-get -yqq update
RUN apt-get -yqq install python3-pip python3-dev curl gnupg
RUN curl -sL https://deb.nodesource.com/setup_10.x | bash

# copy our application code
ADD flask-app /opt/flask-app
WORKDIR /opt/flask-app

# fetch app specific deps
RUN pip3 install -r requirements.txt

# expose port
EXPOSE 5001

# start app
CMD [ "python3", "./myapp.py" ]
