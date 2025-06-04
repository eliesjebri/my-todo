from flask_sqlalchemy import SQLAlchemy

# Création de l'instance globale SQLAlchemy
db = SQLAlchemy()

def init_db(app):
    """
    Initialise la base de données avec l'application Flask.
    """
    db.init_app(app)

    # Crée les tables si elles n'existent pas encore
    with app.app_context():
        db.create_all()

def get_db():
    """
    Fournit une instance de db utilisable ailleurs dans le code.
    """
    return db
