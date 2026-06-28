# FastAPI & ChromaDB File Management API

This is a modular FastAPI backend designed to handle file uploads, metadata storage using ChromaDB, downloading files, and file deletions. It is designed to act as the ingest/storage service for RAG applications.

## Folder Structure

```text
backend/
├── app/
│   ├── __init__.py
│   ├── config.py         # App configuration settings (CORS, folders)
│   ├── database.py       # ChromaDB persistent client setup
│   ├── main.py           # Application entrypoint & global exception handlers
│   ├── routes/
│   │   ├── __init__.py
│   │   └── files.py      # HTTP Endpoint routes (/upload, /get-files, /files/{id})
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── file_schemas.py  # Pydantic validation schemas
│   └── services/
│       ├── __init__.py
│       └── file_service.py # Core business logic (filesystem & DB synchronization)
├── uploads/              # Local storage folder for physical files (created dynamically)
├── chroma_db/            # Local directory for ChromaDB persistence (created dynamically)
├── requirements.txt      # Python dependencies
└── README.md             # This instruction manual
```

## Features

1. **Modular Architecture**: Clean separation of routes, services, schemas, database layers, and storage.
2. **ChromaDB Integration**: Uses persistent local vector storage to manage file metadata.
3. **Collision Resistance**: Uploaded files are stored with unique UUID-based internal filenames while keeping their original filename safe in ChromaDB.
4. **CORS Enabled**: Configured to accept requests from `http://localhost:3000`.
5. **Robust Error Handling**: Standardized responses for 404 (Not Found), 400 (Bad Request), and 500 (Internal Server Error).

---

## Setup & Running Instructions

### 1. Prerequisites
Ensure you have Python 3.9+ installed on your system.

### 2. Create a Virtual Environment (Recommended)
From the `backend` directory, run:
```bash
python -m venv venv
```
Activate it:
- **Windows (Command Prompt)**:
  ```cmd
  venv\Scripts\activate.bat
  ```
- **Windows (PowerShell)**:
  ```powershell
  venv\Scripts\Activate.ps1
  ```
- **Windows (Git Bash)**:
  ```bash
  source venv/Scripts/activate
  ```
- **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies
Run the following command to install the required packages:
```bash
pip install -r requirements.txt
```

### 4. Run the Server
Start the development server using `uvicorn`:
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

The API will now be running on [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## API Documentation

FastAPI automatically generates interactive API documentation. Once the server is running, visit:
* **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Endpoint Details

### 1. Upload File
* **Endpoint**: `POST /upload`
* **Content-Type**: `multipart/form-data`
* **Request Body**: Binary file payload
* **Response**:
  ```json
  {
    "id": "7ca64731-0df0-4b07-ba7b-60b64be872ab",
    "filename": "annual-report.pdf",
    "extension": ".pdf"
  }
  ```

### 2. Get All Files
* **Endpoint**: `GET /get-files`
* **Response**:
  ```json
  [
    {
      "id": "7ca64731-0df0-4b07-ba7b-60b64be872ab",
      "filename": "annual-report.pdf",
      "extension": ".pdf"
    }
  ]
  ```

### 3. Download File
* **Endpoint**: `GET /files/{file_id}`
* **Response**: Returns the raw binary file as an attachment stream.

### 4. Delete File
* **Endpoint**: `DELETE /files/{file_id}`
* **Response**:
  ```json
  {
    "detail": "File 'annual-report.pdf' (ID: 7ca64731-0df0-4b07-ba7b-60b64be872ab) successfully deleted."
  }
  ```
