from typing import List
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    
    # Chroma Cloud connection parameters
    CHROMA_API_KEY: str = "ck-Gf7HcHj655azjCVttGfL7qWgUV2Lyg45S2UBLFrquNDu"
    CHROMA_TENANT: str = "7172d265-1abc-4f7b-bff2-d5ebf87b651a"
    CHROMA_DATABASE: str = "rag"
    OPEN_AI: str = "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"
    
    # Allowed CORS origins
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()

