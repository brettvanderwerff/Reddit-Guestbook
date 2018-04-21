FROM ubuntu:latest
FROM python:latest
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential 
COPY . /rgb
WORKDIR /rgb
RUN pip install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["rgb.py"]
