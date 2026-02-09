FROM python:3.8-slim

WORKDIR /app

<<<<<<< HEAD
# Copy everything
=======
# Add src folder to Python path
ENV PYTHONPATH=/app/src

>>>>>>> c6684b4970d68721b7c1c8a7f12d6c55ac8fd59c
COPY . .

# Install dependencies + your src package
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 7860

CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:7860"]
