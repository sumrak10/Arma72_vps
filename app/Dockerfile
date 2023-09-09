FROM python:3.10

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

RUN sudo snap install --classic certbot

EXPOSE 80 443

CMD ["python", "run.py"]