from flask import Flask
from src.config import Config
from src.routes.todos import todos_bp
from src.persistence.db import init_db

def create_app():
    app = Flask(__name__)

    # Configuration centralisée
    app.config.from_object(Config)

    # Configuration SQLAlchemy explicite
    app.config['SQLALCHEMY_DATABASE_URI'] = Config.DB_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Init DB et routes
    init_db(app)
    app.register_blueprint(todos_bp)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host=Config.HOST, port=Config.PORT)

#from flask import Flask
#from src.config import Config
#from src.routes.todos import todos_bp
#from src.persistence.db import init_db

#def create_app():
#    app = Flask(__name__)
    
    # Chargement de la configuration
#    app.config['SQLALCHEMY_DATABASE_URI'] = Config.DB_URI
#    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#    app.config['ENV'] = Config.ENV
#    app.config['DEBUG'] = Config.DEBUG

    # Initialisation de la base de données
#    init_db(app)

    # Enregistrement des blueprints
#    app.register_blueprint(todos_bp)

#    return app

#if __name__ == "__main__":
#    app = create_app()
#    app.run(host=Config.HOST, port=Config.PORT)
