FROM python:3.8-slim

WORKDIR /app

# 👇 THIS IS THE CRITICAL LINE
ENV PYTHONPATH=/app

COPY . .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 7860

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:7860"]
