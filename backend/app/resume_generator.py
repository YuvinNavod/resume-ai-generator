from docx import Document
from app.ai.summarizer import summarize_text
import os

def create_resume(data) -> dict:
    doc = Document()

    # Header
    doc.add_heading(data.name, 0)
    doc.add_paragraph(data.title)
    doc.add_paragraph(data.contact)
    if data.links:
        doc.add_paragraph(" | ".join(data.links))

    # Summary
    doc.add_heading("Professional Summary", level=1)
    doc.add_paragraph(summarize_text(data.summary))

    # Experience
    doc.add_heading("Experience", level=1)
    for exp in data.experience:
        doc.add_paragraph(f"{exp.job_title}, {exp.company} ({exp.duration})", style="List Bullet")
        doc.add_paragraph(exp.details, style="Normal")

    # Education
    doc.add_heading("Education", level=1)
    for edu in data.education:
        doc.add_paragraph(f"- {edu}")

    # Skills
    doc.add_heading("Technical Skills", level=1)
    doc.add_paragraph(", ".join(data.technical_skills))
    doc.add_heading("Soft Skills", level=1)
    doc.add_paragraph(", ".join(data.soft_skills))

    # Certifications
    if data.certifications:
        doc.add_heading("Certifications", level=1)
        for cert in data.certifications:
            doc.add_paragraph(f"- {cert}")

    # Projects
    if data.projects:
        doc.add_heading("Projects", level=1)
        for project in data.projects:
            doc.add_paragraph(f"- {project}")

    # Languages
    if data.languages:
        doc.add_heading("Languages", level=1)
        doc.add_paragraph(", ".join(data.languages))

    # Save to static
    os.makedirs("static", exist_ok=True)
    filename = f"static/{data.name.replace(' ', '_')}_resume.docx"
    doc.save(filename)

    return {"message": "Resume generated successfully", "file_path": filename}
    

