"""
    data.py: contains all info for rendering
"""
# general
USER_NAME = "abenezer m. mamo"
# social links
social_links = [
    {
        "name": "github",
        "link": "https://github.com/a6enez3r",
        "class": "fa fa-github-square",
    },
    {
        "name": "linked_in",
        "link": "https://www.linkedin.com/in/a6enez3r/",
        "class": "fa fa-linkedin-square",
    },
    {
        "name": "angel",
        "link": "https://angel.co/u/a6enez3r",
        "class": "fa fa-angellist",
    },
    {
        "name": "availability",
        "link": "https://calendly.com/a6enez3r",
        "class": "fa fa-calendar",
    },
]
# work
work_data = [
    {
        "title": "Software Engineer",
        "company": "ForAllSecure",
        "duration": "Mar, 2021 - Present",
        # pylint: disable=line-too-long
        "summary": """designing, building, and maintaining various services and features necessary to bring Mayhem, a fully autonomous cybersecurity system, to market.""",
        "projects": [
            "Reporting Dashboard",
            "Mayhem for CI/CD",
        ],
        "tools": [
            "GKE",
            "python",
            "react",
            "typescript",
            "kubernetes",
            "docker",
            "flask",
            "bash",
            "PostgreSQL",
            "git",
            "selenium",
        ],
    },
    {
        "title": "Junior Backend Developer",
        "company": "Pivony",
        "duration": "May, 2020 - Oct, 2020",
        # pylint: disable=line-too-long
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
        # pylint: disable=line-too-long
        "summary": """researched various topics in CS including but not limited to genetic algorithms, neural networks, robotics, data manipulation, and database management culminating in a final year dissertation exploring the effect of incremental training on word embedding generation.""",
        "projects": ["genetic algorithms", "word embeddings", "NER engine"],
        "tools": ["pyTorch", "python", "spaCy", "anaconda", "MySQL", "Haskell", "git"],
    },
    {
        "title": "Software Engineer Intern",
        "company": "Software Design Studio",
        "duration": "Jan, 2017 - Aug, 2017",
        # pylint: disable=line-too-long
        "summary": """got introduced to web programming tools such as flask, javascript, postgreSQL, HTML/CSS/JavaScript, Git, & Linux and built a fleet management / geolocation tracking web application to efficiently automate vehicle management""",
        "projects": ["geolocation tracking", "user authentication", "CSS Themes"],
        "tools": [
            "flask",
            "HTML",
            "JavaScript",
            "CSS",
            "PostgreSQL",
            "jinja",
            "git",
            "Google Maps API",
        ],
    },
]
# about
about_data = {
    # pylint: disable=line-too-long
    "text": """
                I am a full-stack developer with a strong background in API design & development, microservices, databases, cloud-native & serverless computing, NLP/ML.
            """,
    "projects": [
        {
            "title": "teret",
            "link": "https://github.com/a6enez3r/teret",
            # pylint: disable=line-too-long
            "summary": "blogging application with a WYSIWYG editor built using Flask + SummernoteJS + SQLite (or any other relational database supported by SQLAlchemy)",
        },
        {
            "title": "tunez",
            "link": "https://github.com/a6enez3r/tunez",
            # pylint: disable=line-too-long
            "summary": "web music player built using Flask + HowlerJS + SQLite/SQLAlchemy",
        },
        {
            "title": "mok",
            "link": "https://github.com/a6enez3r/mok",
            # pylint: disable=line-too-long
            "summary": "generate data files. currently supports: JSON, CSV, Parquet, and XLSX",
        },
        {
            "title": "flask_rl",
            "link": "https://github.com/a6enez3r/flask_rl",
            # pylint: disable=line-too-long
            "summary": "rate limiting flask extension",
        },
        {
            "title": "jval",
            "link": "https://github.com/a6enezer/flask_rl",
            "summary": "validate JSON data against a schema",
        },
        {
            "title": "mkd",
            "link": "https://github.com/a6enez3r/mkd",
            # pylint: disable=line-too-long
            "summary": "simplify running common Docker containers",
        },
    ],
}
