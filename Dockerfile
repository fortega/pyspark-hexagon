FROM apache/spark-py:v3.4.0
# USER root
# RUN apt update && apt upgrade -y &&\
#     apt install -y python3-pip

# WORKDIR /app
# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt && rm requirements.txt

COPY src .

# USER 185
# ENTRYPOINT [ ]
CMD [ "/opt/spark/bin/spark-submit", "--packages=org.opensearch.client:opensearch-spark-30_2.12:1.0.1", "main.py" ]