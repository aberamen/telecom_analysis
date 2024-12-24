# Base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy requirements
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port for dashboard
EXPOSE 8050

# Run the dashboard
CMD ["python", "scripts/task_5_dashboard.py"]
