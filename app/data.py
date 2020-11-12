# general
name = "abenezer m. mamo"
# social links
social_links = [
    {"name": "github", "link": "https://github.com/abmamo", "class": "fa fa-github-square"},
    {"name": "linked_in", "link": "https://www.linkedin.com/in/abmamo/", "class": "fa fa-linkedin-square"},
    {"name": "angel", "link": "https://angel.co/u/abmamo", "class": "fa fa-angellist"}
]
# work
work_data = [
    {
        "title": "Junior Backend Developer",
        "company": "Pivony",
        "duration": "May, 2020 - Oct, 2020",
        "summary": """architected a distributed AWS native topic modeling platform to efficiently process and summarize textual data and identify user trends such as sentiment, complaints, influence, keywords, topics, and deliver actionable insights.""",
        "projects": [
            "preprocessing engine",
            "aws resource orchestrator",
            "restful API",
        ],
        "tools": [
            "AWS",
            "python",
            "dask",
            "docker",
            "flask",
            "bash",
            "PostgreSQL",
            "git",
        ],
    },
    {
        "title": "Topics in NLP",
        "company": "Reed College/Univ. of Sussex",
        "duration": "Sep, 2017 - Jan, 2020",
        "summary": """researched various topics in CS including but not limited to genetic algorithms, neural networks, robotics, data manipulation, and database management culminating in a final year dissertation exploring the effect of incremental training on word embedding generation.""",
        "projects": ["genetic algorithms", "word embeddings", "NER engine"],
        "tools": ["pyTorch", "python", "spaCy", "anaconda", "MySQL", "Haskell", "git"],
    },
    {
        "title": "Full Stack Developer Intern",
        "company": "Software Design Studio",
        "duration": "Jan, 2017 - Aug, 2017",
        "summary": """got introduced to web programming tools such as flask, javascript, postgreSQL, HTML/CSS/JavaScript, Git, & Linux and built a fleet management / geolocation tracking web application to efficiently automate vehicle management""",
        "projects": ["geolocation tracking", "user authentication", "CSS Themes"],
        "tools": ["flask", "HTML", "JavaScript", "CSS", "PostgreSQL", "jinja", "git", "Google Maps API"],
    }
]
# about
about_data = {
    "text": """
                I am a full stack developer with strong backgrounds in API design & development, micro services, databases, cloud-native & server less computing, 
                topics in NLP & ML, security, test-driven development, CI/CD pipelines, and agile methodologies. Looking for an opportunity to leverage my skills 
                and experience to build resilient & scalable systems to automate and optimize workflows, extract meaningful insights, and provide intelligent decision making.
            """,
    "projects": [
        {"title": "fs2db", "link": "https://github.com/abmamo/fs2db", "summary": "python package with functions that perform extract + load operations on files and load them to a central db"},
        {"title": "mock", "link": "https://github.com/abmamo/mock", "summary": "currently working on a mock data generation package. supports generating CSV, JSON, Parquet, and SQLite."},
        {"title": "grub", "link": "https://github.com/abmamo/grub",
            "summary":
            """
                a cart management tool written in go and python to make coordinating group orders easy. 
                It is comprised of two RESTful services: a Mux RESTful API to provide an interface to a 
                MongoDB Atlas cluster for storage and a Flask RESTful API for integrations such as slack or a web app. 
                Initially using the go exec command to manually start up the Flask API to interface 
                with slack and serve the UI. Hoping to move to a GRPC based communication.
            """
        },
        {"title": "teret", "link": "https://teret.abmamo.com", "summary": "blogging application with WYSIWYG editor built using Flask + SummernoteJS + SQLite."},
        {"title": "tunez", "link": "https://tunez.abmamo.com", "summary": "music player web application built using Flask + HowlerJS + SQLite/SQLAlchemy"},
    ]
}