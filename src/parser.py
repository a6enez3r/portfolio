"""
    parser.py: autoamtially generate resume info from resume.md using
               BeautifulSoup
"""
from urllib.parse import urlparse

from bs4 import BeautifulSoup


def resume_content(resume_path: str):  # pylint: disable=too-many-locals
    """
    parse the contents of the auto generated resume.html
    we get from running make generate-resume

    params:

    :path resume_path (str): path to resume.html
    """

    with open(resume_path, "rb") as resume_md:
        data = resume_md.read()
    soup = BeautifulSoup(data, "html.parser")
    # links
    links = []
    host2icon = {
        "github.com": "fa fa-github-square",
        "linkedin.com": "fa fa-linkedin-square",
        "abenezer.sh": "fa fa-envelope-o",
        "calendly.com": "fa fa-calendar",
    }
    for item in soup.select("#resume > ul:nth-child(2)"):
        raw = [link.strip() for link in item.get_text().split("\n") if link != ""]
        for link in raw:
            # special processing for email
            if "@" in link:
                host = link[link.index("@") + 1 :]
                # append "mailto:" so clicking on the mail icon
                # open the default mail client
                link = "mailto:" + link
            # all other social links
            else:
                host = urlparse(link).netloc
            links.append(
                {
                    "class": host2icon[host],
                    "link": link,
                }
            )
    # about blurb
    aboutme = ""
    for item in soup.select("#resume > p:nth-child(3)"):
        aboutme += item.get_text()
    # experiences blurb
    exepriences = []
    for item in soup.select("#resume > h3")[:3]:
        raw = [x.strip() for x in item.get_text().split("  ") if x != ""]
        position, company, duration = (
            raw[0].split(",")[0].strip(),
            raw[0].split(",")[1].strip(),
            raw[1].strip(),
        )
        exepriences.append(
            {
                "company": company,
                "position": position,
                "duration": duration,
            }
        )
    for idx, item in enumerate(soup.select("#resume > p")[1 : 3 + 1]):
        exepriences[idx]["description"] = item.get_text()
    return {"aboutme": aboutme, "experiences": exepriences, "links": links}


# UNCOMMENT: the following two lines to debug the parser
#            by running python3 src/parser.py
# from pprint import pprint
# pprint(resume_content("./src/static/resume/resume.html"))
