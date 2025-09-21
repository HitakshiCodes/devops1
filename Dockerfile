# 1. Start from official Python image
FROM python:3.10-slim

# 2. Set working directory in container
WORKDIR /app

# 3. Copy your Python script into the container
COPY hello.py .

# 4. Run the Python script when container starts
CMD ["python", "hello.py"]
