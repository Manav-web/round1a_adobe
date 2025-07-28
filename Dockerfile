FROM python:3.9-slim

WORKDIR /app

# Copy entire app folder (including requirements.txt)
COPY app/ /app/app/

# Install Python dependencies from inside the container
RUN pip install --no-cache-dir -r /app/app/requirements.txt

# Set default command to run your app
CMD ["python", "app/main.py"]
