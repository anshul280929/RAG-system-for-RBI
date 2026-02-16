import os
from dotenv import load_dotenv
from pathlib import Path

# Get project root directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Load .env from root
load_dotenv(BASE_DIR / ".env")


class Settings:
    def __init__(self):
        self.NEO4J_URI = os.getenv("NEO4J_URI")
        self.NEO4J_USER = os.getenv("NEO4J_USER")
        self.NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")


settings = Settings()
