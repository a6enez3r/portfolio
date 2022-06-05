"""
    wsgi.py: app entry point
"""
import os

from dotenv import load_dotenv

from src.factory import create_app

# load env vars
load_dotenv()
# [OPTIONAL] get GitHub creds to automatically display repos
gh_pat, gh_username = os.environ.get("GH_PAT", None), os.environ.get("GH_USERNAME", None)
# create WSGI app
app = create_app(
    environment=os.environ.get("ENVIRONMENT", "development")
)
# if executed as script (in dev / testing)
if __name__ == "__main__":
    app.run(host=os.environ.get("HOST", "0.0.0.0"), port=int(os.environ.get("PORT", 5000)))
