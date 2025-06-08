from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier `.env.<ENV>`
env_name = os.getenv("ENV", "development")
dotenv_path = f"/app/config/.env.{env_name}"

if not os.path.exists(dotenv_path):
    raise FileNotFoundError(f"Fichier .env non trouvé : {dotenv_path}")

load_dotenv(dotenv_path)


class Config:
    ENV = env_name
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
    HOST = os.getenv("HOST", "0.0.0.0")
    PORT = int(os.getenv("PORT", 5000))
    VERSION = os.getenv("VERSION", "1.0.0")


def get_db_uri():
    if Config.ENV in ["production", "staging"]:
        user = os.getenv("MYSQL_USER")
        password = os.getenv("MYSQL_PASSWORD")
        host = os.getenv("MYSQL_HOST")
        port = os.getenv("MYSQL_PORT")
        db = os.getenv("MYSQL_DB")
        return f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
    else:
        return os.getenv("SQLITE_URI")


db_uri = get_db_uri()
if not db_uri:
    raise ValueError("DB_URI est vide. Vérifie les variables d'environnement.")
Config.DB_URI = db_uri
