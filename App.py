from pathlib import Path

import streamlit as st
from PIL import Image

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
Web-developer, data-engineer, and software developer
"""
EMAIL = "Grantmelvin4@gmail.com"
SOCIAL_MEDIA = {
    "Github": "https://github.com/GrantMelvin",
    "LinkedIn": "https://www.linkedin.com/in/grant-melvin-905783229/"
}
PROJECTS = {
    "📊 ECUQuestCS - A study tool for CS": "https://github.com/GrantMelvin/ECUQuestCS",
    "📂 Student Management System - An organizational tool for teachers": "https://github.com/GrantMelvin/StudentManagementSystem.io"
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
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application.octet-stream",
    )
    st.write("📭", EMAIL)

# Social Links
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# Experience
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
"""
- ✅ 4 Years of software development experience through coursework and professional experiences
- ✅ Accustomed to being a team leader by managing goals, workflows, and development roadblocks
- ✅ Adaptive to needs of the position by learning new technologies and seeking out ways to improve
""")

# Skills
st.write("#")
st.subheader("Hard Skills")
st.write(
"""
- 🧑‍💻 Languages: C++, Python, Java, Javascript
- 🪟 Frameworks: React, Node
- 📦 Databases: PostgreSQL, SQL
- 📊 Technologies: Github, Docker, Solr        
""")

# Work History
st.write("#")
st.subheader("Work History")
st.write("---")

# Job 1
st.write("#")
st.write("🚧", "Lead Research Assistant | East Carolina University - Department of Defense")
st.write("08/2023 - 12/2023")
st.write(
"""
- ➡️
- ➡️ 
- ➡️
"""
)

