FROM python:3-alpine

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt && rm requirements.txt

COPY main.py main.py
COPY src src

CMD [ "python3", "main.py"]