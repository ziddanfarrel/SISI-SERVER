# Gunakan Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file aplikasi ke dalam container
COPY . /code/

# Perintah untuk menjalankan Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
