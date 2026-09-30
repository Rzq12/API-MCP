import os
from dataclasses import dataclass
from dotenv import load_dotenv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[3]
load_dotenv(PROJECT_ROOT / ".env")

@dataclass(frozen=True)
class Settings:
    bkn_api_base_url: str = os.getenv("BKN_API_BASE_URL", "https://api-dashboard.lan.go.id")

settings = Settings()
