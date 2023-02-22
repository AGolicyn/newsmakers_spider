FROM python:3.10-buster

WORKDIR /src/parsing


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./spider/requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./spider .


#ENTRYPOINT "python" "/src/parsing/spider/spiders/my_spiders/main.py"
