FROM python:3.8-slim

WORKDIR /app

# Add src folder to Python path
ENV PYTHONPATH=/app/src

COPY . .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 7860

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:7860"]
