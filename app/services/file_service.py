import uuid
import os
from typing import List, Dict, Any
from fastapi import UploadFile
from app.database import get_collection

class FileService:
    def __init__(self):
        self.collection = get_collection()

    def upload_file(self, file: UploadFile) -> Dict[str, Any]:
        file_id = str(uuid.uuid4())
        
        # Extract filename and extension
        original_filename = file.filename
        extension = os.path.splitext(original_filename)[1]
        self.collection.add(
            ids=[file_id],
            metadatas=[{
                "filename": original_filename,
                "extension": extension
            }],
            documents=[original_filename]
        )
            
        return {
            "id": file_id,
            "filename": original_filename,
            "extension": extension
        }

    def get_all_files(self) -> List[Dict[str, Any]]:
        results = self.collection.get()
            
        files = []
        ids = results.get("ids", [])
        metadatas = results.get("metadatas", [])
        
        for idx, file_id in enumerate(ids):
            metadata = metadatas[idx]
            files.append({
                "id": file_id,
                "filename": metadata.get("filename", ""),
                "extension": metadata.get("extension", "")
            })
        return files

    def get_file_metadata(self, file_id: str) -> Dict[str, Any]:
        result = self.collection.get(ids=[file_id])
            
        if not result.get("ids"):
            raise FileNotFoundError(f"File with ID '{file_id}' not found in metadata database.")
            
        metadata = result["metadatas"][0]
        return {
            "id": file_id,
            "filename": metadata.get("filename", ""),
            "extension": metadata.get("extension", "")
        }

    def delete_file(self, file_id: str) -> Dict[str, Any]:
        metadata = self.get_file_metadata(file_id)
        self.collection.delete(ids=[file_id])
            
        return {
            "id": file_id,
            "filename": metadata.get("filename", "")
        }
