FROM python:3.8-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Hugging Face requires port 7860
EXPOSE 7860

# Start Flask app with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:7860", "app:app"]
