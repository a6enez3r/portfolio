# set base image (host OS)
FROM python:3.9
# set the working directory in the container
WORKDIR /app
# update linux installer
RUN apt update
# upgrade default packages
RUN apt -y upgrade
# install pip
RUN apt install -y python3-pip
# install python deps
RUN apt install build-essential -y --no-install-recommends
# copy the contents of the local app directory to the working directory
# need to be really careful to not accidentally add sensitive info such
# as .env files
COPY src src
COPY wsgi.py wsgi.py
COPY requirements.txt requirements.txt
COPY tests tests
# upgrade pip
RUN pip3 install --upgrade pip
# install python deps
RUN pip3 install -r requirements.txt
# run app
CMD [ "make", "dev"]