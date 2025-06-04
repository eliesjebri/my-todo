import os
from dotenv import load_dotenv
from pathlib import Path

# Détecter l'environnement actif
ENV = os.getenv("ENV", "development").lower()

# Charger le bon fichier .env depuis le dossier config/
env_path = Path(__file__).resolve().parents[2] / "config" / f".env.{ENV}"
load_dotenv(dotenv_path=env_path)

class Config:
    ENV = ENV
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 5000))
    VERSION = os.getenv("VERSION", "1.0.0")

    if ENV in ["production", "staging"]:
        DB_URI = (
            f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}"
            f"@{os.getenv('MYSQL_HOST')}:{os.getenv('MYSQL_PORT')}/{os.getenv('MYSQL_DB')}"
        )
    else:
        DB_URI = os.getenv("SQLITE_URI", "sqlite:///data.db")
