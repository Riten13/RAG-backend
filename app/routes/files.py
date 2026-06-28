from typing import List
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException, status
from fastapi.responses import FileResponse
from app.schemas.file_schemas import FileMetadataResponse
from app.services.file_service import FileService

router = APIRouter()

def get_file_service():
    return FileService()

@router.post("/upload",response_model=FileMetadataResponse)
def upload_file(file: UploadFile = File(...), service = Depends(FileService)):
    return service.upload_file(file)

@router.get("/get-files", response_model=List[FileMetadataResponse])
def get_all_files(service= Depends(FileService)):
    return service.get_all_files()

@router.get("/files/{file_id}")
def download_file( file_id: str, service = Depends(FileService)):
    file_path = service.get_file_path(file_id)
    metadata = service.get_file_metadata(file_id)
    return FileResponse(
        path=file_path,
        filename=metadata["filename"],
        media_type="application/octet-stream"
    )

@router.delete("/files/{file_id}")
def delete_file( file_id: str, service= Depends(FileService)):
    result = service.delete_file(file_id)
    return {"detail": f"File '{result['filename']}' (ID: {file_id}) successfully deleted."}
