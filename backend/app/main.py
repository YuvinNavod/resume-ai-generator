from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
from app.models import ResumeRequest
from app.resume_generator import create_resume
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Allow frontend requests during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# CSP Middleware
class CSPMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response: Response = await call_next(request)
        response.headers["Content-Security-Policy"] = (
            "default-src 'self'; script-src 'self'; style-src 'self' 'unsafe-inline';"
        )
        return response

app.add_middleware(CSPMiddleware)

@app.post("/generate-resume/")
def generate(resume: ResumeRequest):
    return create_resume(resume)

@app.get("/download-resume/{filename}")
def download_resume(filename: str):
    file_path = os.path.join("static", filename)
    if os.path.exists(file_path):
        return FileResponse(
            path=file_path,
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            filename=filename
        )
    return {"error": "File not found"}

