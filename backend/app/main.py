from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models import ResumeRequest
from app.resume_generator import create_resume
from fastapi.responses import FileResponse
import os


app = FastAPI()

# Allow frontend requests during development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

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

