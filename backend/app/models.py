from pydantic import BaseModel, EmailStr, HttpUrl, constr, Field    
from typing import List, Optional

class Experience(BaseModel):
    job_title: str
    company: str
    from_month: str
    from_year: str
    to_month: str
    to_year: str
    details: str

class Degree(BaseModel):
    degree: str

class NamedItem(BaseModel):
    name: str

class Link(BaseModel):
    url: str

class ResumeRequest(BaseModel):
    name: str
    title: str
    summary: str
    phone: str
    email: str
    address: str
    linkedin: Optional[str] = None
    github: Optional[str] = None
    experience: List[Experience]
    education: List[Degree]
    technical_skills: List[NamedItem]
    soft_skills: List[NamedItem]
    certifications: List[NamedItem]
    projects: List[NamedItem]
    languages: List[NamedItem]
    links: List[Link]
