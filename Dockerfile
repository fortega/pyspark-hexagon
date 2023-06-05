FROM apache/spark-py:v3.4.0
USER root
RUN apt update && apt upgrade -y &&\
    apt install -y python3-pip

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt && rm requirements.txt

USER 1000

COPY src src

CMD [ "python3", "src/main.py"]