import uuid
import hashlib
from fastapi import UploadFile

async def generate_file_id(file: UploadFile) -> str:
    content = await file.read()
    return hashlib.md5(content).hexdigest()