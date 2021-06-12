"""
    data.py: contains all info for rendering
"""
# general
USER_NAME = "abenezer m. mamo"
# social links
social_links = [
    {
        "name": "github",
        "link": "https://github.com/abmamo",
        "class": "fa fa-github-square",
    },
    {
        "name": "linked_in",
        "link": "https://www.linkedin.com/in/abmamo/",
        "class": "fa fa-linkedin-square",
    },
    {"name": "angel", "link": "https://angel.co/u/abmamo", "class": "fa fa-angellist"},
    {
        "name": "availability",
        "link": "https://calendly.com/abenezermamo",
        "class": "fa fa-calendar",
    },
]
# work
work_data = [
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
        "title": "Full Stack Developer Intern",
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
    "text": """
                I am a full stack developer with strong backgrounds in API design & development, micro services, databases, cloud-native & server less computing, 
                topics in NLP & ML, security, test-driven development, CI/CD pipelines, and agile methodologies. Looking for an opportunity to leverage my skills 
                and experience to build resilient & scalable systems to automate and optimize workflows, extract meaningful insights, and provide intelligent 
                decision making.

            """,
    "projects": [
        {
            "title": "validate_json",
            "link": "https://github.com/abmamo/validate_json",
            # pylint: disable=line-too-long
            "summary": "validate JSON data against a schema",
        },
        {
            "title": "mock",
            "link": "https://github.com/abmamo/mock",
            # pylint: disable=line-too-long
            "summary": "python package to generate mock data. supports generating CSV, JSON, Parquet, and SQLite.",
        },
        {
            "title": "fastdb",
            "link": "https://github.com/abmamo/fastdb",
            # pylint: disable=line-too-long
            "summary": "python package to easily set up mock Postgres & MySQL databases in docker (requires docker)",
        },
        {
            "title": "flask_rl",
            "link": "https://github.com/abmamo/flask_rl",
            "summary": """
                flask rate limiter extension with an in memory DB
            """,
        },
        {
            "title": "teret",
            "link": "https://teret.abmamo.com",
            # pylint: disable=line-too-long
            "summary": "blogging application with WYSIWYG editor built using Flask + SummernoteJS + SQLite.",
        },
        {
            "title": "tunez",
            "link": "https://tunez.abmamo.com",
            # pylint: disable=line-too-long
            "summary": "music player web application built using Flask + HowlerJS + SQLite/SQLAlchemy",
        },
    ],
}
