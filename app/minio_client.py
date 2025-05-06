from fastapi import FastAPI, UploadFile, File
from minio import Minio
import os

app = FastAPI()

client = Minio(
    endpoint=os.getenv("MINIO_ENDPOINT", "minio:9000").replace("http://", ""),
    access_key=os.getenv("MINIO_ACCESS_KEY", "admin"),
    secret_key=os.getenv("MINIO_SECRET_KEY", "supersecret"),
    secure=False
)

if not client.bucket_exists('uploads'):
    client.make_bucket('uploads')