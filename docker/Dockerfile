# Ubuntu image based on the 21.04 base Ubuntu image

FROM ubuntu:latest

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN pip3 install setuptools

VOLUME [ "/root/SH4D0W" ]
WORKDIR /root/SH4D0W