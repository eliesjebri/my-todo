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


# 🔧 Calcul de la DB_URI après la classe, une fois Config.ENV défini
def get_db_uri():
    if Config.ENV == "production":
        user = os.getenv("MYSQL_USER")
        password = os.getenv("MYSQL_PASSWORD")
        host = os.getenv("MYSQL_HOST")
        port = os.getenv("MYSQL_PORT")
        db = os.getenv("MYSQL_DB")
        return f"mysql+pymysql://{user}:{password}@{host}:{port}/{db}"
    else:
        return os.getenv("SQLITE_URI")


# Injection dynamique de DB_URI dans la classe
Config.DB_URI = get_db_uri()
