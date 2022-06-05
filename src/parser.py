from bs4 import BeautifulSoup
from urllib.parse import urlparse

def resume_content(resume_path):
    """parse the contents of the auto generated resume.html
    we get from running make generate-resume

    params:

    :path resume_path (str): path to resume.html
    """
    data = open(resume_path, "r").read()
    soup = BeautifulSoup(data, "html.parser")
    # links
    links = []
    link_icons = {
        "github.com": "fa fa-github-square",
        "linkedin.com": "fa fa-linkedin-square",
        "abenezer.sh": "fa fa-envelope-o",
        "calendly.com": "fa fa-calendar"
    }
    for item in soup.select("#resume > ul:nth-child(2)"):
        raw = [link.strip() for link in item.get_text().split("\n") if link != '']
        for link in raw:
            if "@" in link:
                host = link[link.index('@') + 1 : ]
                link = "mailto:" + link
            else:
                host = urlparse(link).netloc
            links.append({
                "class": link_icons[host],
                "link": link,
            })
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
