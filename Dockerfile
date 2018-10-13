FROM python:3.6

RUN apt-get update && \
    apt-get install -y libopus0 ffmpeg \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python", "-u", "bot.py"]


