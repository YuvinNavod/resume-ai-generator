from pydantic import BaseModel
from typing import List


class NameEntry(BaseModel):
    name: str

class UrlEntry(BaseModel):
    url: str

class ExperienceEntry(BaseModel):
    job_title: str
    company: str
    from_month: str
    from_year: str
    to_month: str
    to_year: str
    details: str

class ResumeRequest(BaseModel):
    name: str
    title: str
    summary: str
    phone: str
    email: str
    address: str
    linkedin: str
    github: str
    experience: List[ExperienceEntry]
    education: List[dict]
    technical_skills: List[NameEntry]
    soft_skills: List[NameEntry]
    certifications: List[dict]
    projects: List[dict]
    languages: List[dict]
    links: List[UrlEntry]



    
