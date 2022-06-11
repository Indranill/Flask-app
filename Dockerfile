FROM python:3.8.8-slim
WORKDIR /flask-docker
COPY requirenment.txt requirenment.txt
#RUN apt-get -y install python3-pip
RUN pip3 install -r requirenment.txt
COPY ./ ./
CMD [ "python3", "app.py"]
