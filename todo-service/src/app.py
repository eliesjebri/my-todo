from flask import Flask
from flask_cors import CORS
from src.config import Config
from src.routes.todos import todos_bp
from src.persistence.db import init_db

# ✅ Modification ici : accepte un paramètre (même si inutilisé)
def create_app(config=None):
    app = Flask(__name__)

    # ✅ CORS autorisé pour tous les chemins et toutes les origines (dev uniquement)
    CORS(app, resources={r"/*": {"origins": "*"}})

    # ✅ Chargement de la configuration
    app.config.from_object(Config)
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # ✅ Initialisation de la base de données et enregistrement des routes
    init_db(app)
    app.register_blueprint(todos_bp)

    return app

# ✅ Point d’entrée pour le mode standalone (développement uniquement)
if __name__ == "__main__":
    app = create_app()
    app.run(host=Config.HOST, port=Config.PORT)
