# Base Image
FROM python:3.12-slim

# Working Directory
WORKDIR /app

# Copy dependency file first
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project
COPY . .

# Tell Docker which port Flask uses
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]