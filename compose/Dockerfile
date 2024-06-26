FROM python:3.12-slim-bullseye

RUN apt-get -y update && \
    apt-get install -y ffmpeg libsm6 libxext6

WORKDIR /app

COPY compose/requirements.txt requirements.txt

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY app .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
