from pydantic import BaseModel
from typing import List, Optional, Dict

class ExperienceEntry(BaseModel):
    job_title: str
    company: str
    duration: str
    details: str

class ResumeRequest(BaseModel):
    name: str
    contact: str
    title: str
    summary: str
    experience: List[ExperienceEntry]
    education: List[str]
    technical_skills: List[str]
    soft_skills: List[str]
    certifications: Optional[List[str]] = []
    projects: Optional[List[str]] = []
    languages: Optional[List[str]] = []
    links: Optional[List[str]] = []
