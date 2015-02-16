FROM ubuntu:14.04
MAINTAINER d.kershaw1@lancaster.ac.uk

COPY . /code
WORKDIR /code

# Install Python Setuptools
RUN apt-get install -y python-setuptools

# Install pip
RUN easy_install pip
RUN apt-get update && apt-get install -y curl lsb-release supervisor openssh-server
RUN service supervisor restart
RUN pip install -r requirements.txt

RUN cp ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN mkdir /var/log/supervisord/
VOLUME ["/var/log/supervisord/"]

USER root
CMD ["/usr/bin/supervisord"]