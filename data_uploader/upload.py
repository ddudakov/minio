import os
import boto3
from botocore.client import Config

# Настройки MinIO
MINIO_URL = os.getenv('MINIO_URL', 'http://localhost:9000')
MINIO_ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY', 'denis')
MINIO_SECRET_KEY = os.getenv('MINIO_SECRET_KEY', 'ddudakov')
BUCKET_NAME = os.getenv('BUCKET_NAME', 'test-bucket')

# Инициализация клиента S3
s3 = boto3.client(
    's3',
    endpoint_url=MINIO_URL,
    aws_access_key_id=MINIO_ACCESS_KEY,
    aws_secret_access_key=MINIO_SECRET_KEY,
    config=Config(signature_version='s3v4')
)

# Создание бакета
s3.create_bucket(Bucket=BUCKET_NAME)

# Загрузка данных
for i in range(100):
    data = f"data_{i}" * 1024 * 1024 # Генерация данных
    s3.put_object(Bucket=BUCKET_NAME, Key=f"file_{i}.txt", Body=data)
    print(f"Uploaded file_{i}.txt")