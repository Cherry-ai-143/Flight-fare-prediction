# Base image
FROM python:3.8-slim

# Set working directory
WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the project
COPY . .

# Expose port (optional but good practice)
EXPOSE 5000

# Start app using Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]
