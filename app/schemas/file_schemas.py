from pydantic import BaseModel

class FileMetadataResponse(BaseModel):
    id: str
    filename: str
    extension: str

    model_config = {
        "json_schema_extra": {
            "example": {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "filename": "report.pdf",
                "extension": ".pdf"
            }
        }
    }
