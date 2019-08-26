
FROM ubuntu:latest

USER root

RUN apt-get update
RUN apt-get install -y nginx nodejs


RUN rm -v /etc/nginx/nginx.conf


ADD nginx/nginx.conf /etc/nginx/
ADD nginx/mime.types /etc/nginx/

ADD /templates /usr/share/nginx/html/
ADD /templates /var/www/html/


RUN echo "daemon off;" >> /etc/nginx/nginx.conf


CMD service nginx start
