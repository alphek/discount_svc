FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /discount_svc
COPY requirements.txt /discount_svc/
RUN pip install -r requirements.txt
COPY . /discount_svc/