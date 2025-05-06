import io
import uuid
import datetime
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from app.database import SessionLocal
from app.minio_client import client
from app.config import settings
from app.models import FileMetadata
from app.schemas import FileResponse
from app.utils import generate_file_id

from sqlalchemy.orm import Session


router = APIRouter()

async def generate_file_id(file: UploadFile):
    return str(uuid.uuid4())

def check_file_exists(db: Session, file_id: str):
    return db.query(FileMetadata).filter(FileMetadata.id == file_id).first() is not None

@router.post("/upload", response_model=FileResponse)
async def upload_file(file: UploadFile = File(...)):
    if file.content_type not in ["image/jpeg", "image/png", "application/pdf", "application/dicom"]:
        raise HTTPException(status_code=400, detail="Unsupported file format")

    file_id = await generate_file_id(file)
    await file.seek(0)
    content = await file.read()

    client.put_object(
        settings.MINIO_BUCKET_NAME,
        file_id,
        io.BytesIO(content),
        length=len(content),
        content_type=file.content_type
    )

    url = f"{settings.MINIO_ENDPOINT}/{settings.MINIO_BUCKET_NAME}/{file_id}"

    db = SessionLocal()

    if check_file_exists(db, file_id):
        
        db.query(FileMetadata).filter(FileMetadata.id == file_id).update({
            FileMetadata.filename: file.filename,
            FileMetadata.content_type: file.content_type,
            FileMetadata.size: len(content),
            FileMetadata.url: url,
            FileMetadata.created_at: datetime.datetime.utcnow()
        })
    else:
        metadata = FileMetadata(
            id=file_id,
            filename=file.filename,
            content_type=file.content_type,
            size=len(content),
            url=url,
            created_at=datetime.datetime.utcnow()
        )
        db.add(metadata)

    db.commit()
    db.close()

    return {"id": file_id, "url": url}