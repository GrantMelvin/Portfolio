from pathlib import Path

import streamlit as st
from PIL import Image

# Dummy Commit 5
# Path Settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "Styles" / "main.css"
resume_file = current_dir / "Assets" / "Resume.pdf"
profile_pic = current_dir / "Assets" / "profile-pic.png"

# General Settings
PAGE_TITLE = "Digital Resume | Grant Melvin"
PAGE_ICON = ":computer:"
NAME = "Grant Melvin"
DESCRIPTION = """
Aspiring web-developer, data analyst, and software engineer
"""
EMAIL = "Grantmelvin4@gmail.com"
SOCIAL_MEDIA = {
    "Github": "https://github.com/GrantMelvin",
    "LinkedIn": "https://www.linkedin.com/in/grant-melvin-905783229/" 
}
PROJECTS = {
    "📊 ECUQuestCS - A study tool for Computer Science": "https://github.com/GrantMelvin/ECUQuestCS",
    "📂 Student Management System - An organizational tool for teachers": "https://github.com/GrantMelvin/StudentManagementSystem.io",
    "💼 Portfolio Website - A showcase of my abilities": "https://github.com/GrantMelvin/Portfolio"
}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Loading CSS
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# Hero Section
col1, col2 = st.columns(2, gap='small')
with col1:
    st.image(profile_pic, width=300)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📝 Download Resume",
        data=PDFbyte,
        file_name="Grant-Melvin-" + resume_file.name,
        mime="application.octet-stream",
    )
    st.write("📭", EMAIL)

# Social Links
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# Statement of Purpose
st.write("#")
st.subheader("Personal Statement")
st.write(
"""
Hey! I'm Grant, and I sincerely appreciate your visit to my portfolio website. 
Crafted with the intention of transforming my resume into a dynamic showcase, this platform delves into my professional journey, highlighting key work experiences and projects. It's not just a presentation; it's a journey of learning and growth as I explore new technologies. 
Powered by the Python library Streamlit, this site is hosted on an AWS EC2 instance. 
Welcome to the intersection of my creativity and professional experiences!
""")

# Experience
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
"""
- ✅ 3 Years of software development experience through coursework and jobs
- ✅ Skilled in team leading by managing goals, workflows, and development hurdles
- ✅ Adaptable to role needs through continuous learning and pursuit of improvement
""")

# Skills
st.write("#")
st.subheader("Skills")
st.write(
"""
- 🧑‍💻 Languages: C++, Python, Java, Javascript
- 🪟 Frameworks: React, Node, Express
- 📦 Databases: PostgreSQL, SQL
- 📊 Technologies: Github, Docker, Solr        
""")

# Work History
st.write("#")
st.subheader("Work History")

# Job 1
st.write("🚧", "Lead Research Assistant | East Carolina University - Department of Defense")
st.write("08/2023 - 12/2023")
st.write(
"""
- ➡️ Collaborated with a Department of Defense client on an application focused on leveraging bulk data for
enhanced decision-making capabilities.
- ➡️ Orchestrated the end-to-end development, integration, and containerization of an application, ensuring accessibility and tailored functionality for the client.
- ➡️ Coordinated regular meetings with colleagues to discuss project objectives, milestones, and challenges,
fostering a collaborative environment that encouraged open communication and shared insights.
- ➡️ Conducted and led presentations to stakeholders, effectively communicating project progress, key
achievements, and addressing any concerns or questions.

"""
)

# Job 2
st.write("#")
st.write("🚧", "Teaching Assistant | East Carolina University")
st.write("03/2022 - Present")
st.write(
"""
- ➡️ Solely responsible for instructing and mentoring 20-40 beginner computer science students, providing comprehensive lessons on fundamental concepts in C/C++ programming languages.
- ➡️ Conducted regular assessments, graded assignments, and provided constructive feedback to support student learning and development.
- ➡️ Attended and actively contributed to professional development meetings, collaborating with colleagues to
discuss student progress, share best practices, and refine instructional strategies.
"""
)

# Job 3
st.write("#")
st.write("🚧", "IT Service Desk Specialist | East Carolina University")
st.write("10/2022 - 08/2023")
st.write(
"""
- ➡️ Conducted troubleshooting to resolve hardware and software issues for ECU students, faculty, and staff.
- ➡️ Acted as a single point of contact for managing telecommunications, networking, and other services from
installation to maintenance.
"""
)

# Projects
st.write("#")
st.subheader("Projects")
for(project, link) in PROJECTS.items():
    st.write(f"[{project}]({link})")