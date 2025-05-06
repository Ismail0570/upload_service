import os

class Settings:
    POSTGRES_URL = os.getenv("POSTGRES_URL", "postgresql://postgres:supersecret1233@db:5432/postgres")
    MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT", "minio:9000")
    MINIO_ACCESS_KEY = os.getenv("MINIO_ACCESS_KEY", "admin")
    MINIO_SECRET_KEY = os.getenv("MINIO_SECRET_KEY", "supersecret")
    MINIO_BUCKET_NAME = os.getenv("MINIO_BUCKET_NAME", "uploads")

settings = Settings()