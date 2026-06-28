from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from app.config import settings
from app.routes.files import router as files_router
from app.ai_chat.chat import router as aibot_router


app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(files_router)
app.include_router(aibot_router)

@app.get("/")
async def root():
    return {
        "message": "Welcome to the File Management API. View the interactive Swagger documentation at /docs."
    }

