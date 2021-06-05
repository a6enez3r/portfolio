"""
    wsgi.py: app entry point
"""
# app factory/creation function
from src.factory import create_app

# env manager
from dotenv import load_dotenv

# os
import os

# load env vars
load_dotenv()
# create app
app = create_app(
    # get environment or use development as default
    environment=os.getenv("ENVIRONMENT", "development")
)
# if executed as script (in dev / testing)
if __name__ == "__main__":
    # run app
    app.run(host=os.getenv("HOST", "0.0.0.0"), port=int(os.getenv("PORT", 5000)))
