# Docker based on Centos7
FROM python:3

RUN mkdir /app

WORKDIR /app

COPY api.py .

RUN pip install flask

CMD ["python3", "api.py"]

EXPOSE 5000
