FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN mkdir -p ./logs

RUN pip install -r requirements.txt

CMD ["python", "-u", "bot.py"]
