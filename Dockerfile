# Dockerfile
FROM python:3.7-buster


# Install RabbitMQ
RUN echo 'deb http://www.rabbitmq.com/debian/ testing main' | tee /etc/apt/sources.list.d/rabbitmq.list
RUN wget -O- https://www.rabbitmq.com/rabbitmq-release-signing-key.asc | apt-key add -
RUN apt-get update
RUN apt-get -y install rabbitmq-server

#install mysql
RUN apt-get -y install mariadb-server
# Create database
RUN /etc/init.d/mysql start && mysql -u root -e "CREATE DATABASE service_monitor"

# copy source and install dependencies
RUN mkdir -p /opt/app
COPY ./requirements/ /opt/app/requirements/
WORKDIR /opt/app
RUN pip install -r requirements/dev.txt

ADD . /opt/app
ADD ./scripts /scripts
ADD ./csv /csv

RUN chmod +x /scripts/start.sh


# start server
EXPOSE 8000
STOPSIGNAL SIGTERM
CMD ["/scripts/start.sh"]