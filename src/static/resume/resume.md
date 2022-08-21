<!-- The (first) h1 will be used as the <title> of the HTML page -->
# Abenezer Mamo

<!-- The unordered list immediately after the h1 will be formatted on a single
line. It is intended to be used for contact details -->
- [https://github.com/a6enez3r](https://github.com/a6enez3r)
- [https://linkedin.com/in/a6enez3r](https://linkedin.com/in/a6enez3r)
- [hi@abenezer.sh](mailto:hi@abenezer.sh)
- [https://calendly.com/a6enez3r](https://calendly.com/a6enez3r)

<!-- The paragraph after the h1 and ul and before the first h2 is optional. It
is intended to be used for a short summary. -->
full-stack developer with backgrounds in API & UI development, microservices, databases, fuzzing, NLP & ML, UX design & research, and cloud-native & bare-metal multi-tenant computing systems

## SKILLS

- **Languages + Frameworks**: Python, JavaScript/TypeScript, Go, Haskell, C++, SQLAlchemy, Flask, Django, React
- **Infra + Ops**: AWS, GCP, Azure, Postgres, MySQL, Mongo, Redis, RabbitMQ, Pulsar, Docker, Kubernetes, Linux, Terraform

## EXPERIENCE

<!-- You have to wrap the "left" and "right" half of these headings in spans by
hand -->
### <span>Software Engineer - Mobile, Klaviyo </span> <span>May 2022 – Present</span>

Collaborating radically on various projects aimed at providing a scalable and performant sending experience necessary to ensure messages sent by clients get sent through the right channel and delivered via the right platform at the right time -- emphasis on internal and external delivery enablement.

- Working with stakeholders across the company to build and manage Klaviyo’s SMS service and learning about the entire software development lifecycle from problem definition to design, development, testing, demoing, and supporting features in production at scale
- Maintaining a customizable account information report generator & visualizer built using vaex, React, Django & MySQL to quickly identify and decommission low-volume and noncompliant SMS accounts & reduce costs associated with unused numbers & content violation remediation fees
- Working on internal tooling such as docd - a lightweight python CLI that leverages ASTs and integrates with pre-commit hooks to simplify autogenerating docstring placeholders as well as writing internal documentation and incrementally improving code readability in a sizeable monolithic codebase
- Debugging, troubleshooting, and fixing various operational issues and bugs that come up during pager duty

### <span>Software Engineer - Platform, ForAllSecure </span> <span>March 2021 – May 2022</span>

Worked independently and as part of short-term & rapidly evolving teams to bring Mayhem -- a fully autonomous cybersecurity system -- to market. Responsibilities included but were not limited to designing, building, and maintaining various services and features, such as GitHub OAuth and sharable badges, aimed at enabling easy integration into existing CI/CD pipelines and shortening customer onboarding journeys.

- Integrate third-party APIs such as GitHub OAuth & Keycloak to simplify authentication in CI/CD workflows
- Optimized queries associated with defect reporting endpoints to decrease page load times by 24%
- Built a reporting dashboard using Postgres, SQLAlchemy & React (reCharts) to provide easily consumable usage insights and increase engagement with non-developer users of the Mayhem platform
- Actively improved internal testing infrastructure using pytest fixtures to increase reusability & test coverage by 8%
- Refactored database garbage collector queries to minimize the number of test cases stored in a database without adversely affecting coverage to provide faster test suite download and regression testing times for customers

### <span>Junior Backend Engineer, Pivony </span> <span>May 2020 – October 2020</span>

Architected a distributed AWS native topic modeling platform to process and summarize textual data, identify trends such as sentiment, common complaints, influential documents, most frequent keywords, and deliver actionable insights.

- Built a preprocessing microservice using SQLAlchemy, Docker, and Dask to provide multilingual sentiment analysis, text tokenization, & keyword extraction; optimized the service using multithreading, resulting in a 55% reduction in billable EC2 instance hours
- Created an AWS resource orchestrator using boto3, SQLAlchemy, and Postgres to optimize resource allocation and eliminate idle EC2 instances
- Researched and developed a topic modeling engine utilizing BERT and various unsupervised algorithms such as LDA & GSDMM to cluster text into human-readable topics at scale
- Designed and implemented a RESTful API to provide a universal gateway to various microservices using Nginx, Flask, SQLAlchemy, and AWS RDS

## EDUCATION

### <span>Computer Science, BA, Reed College</span> <span>August 2015 – January 2020</span>

- **Thesis** : Scalable Learning for the Odd-Man-Out Task with Applications to Word Vector Induction

### <span>Study Abroad, Informatics</span> <span>August 2017 – June 2018</span>

## PROJECTS

### <span>mok</span> <span>November 2020 – Present</span>

- A pseudo-random data file [CSV, JSON, Parquet, XLSX, TXT] generator package written in Python

### <span>sirch</span> <span>June 2022 – Present</span>

- Parse static Markdown files & extract metadata such as keywords, tags, and summaries using natural language processing libraries to generate a low-bandwidth searchable static site
