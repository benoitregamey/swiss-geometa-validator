from flask import Flask
import os 

def create_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)

    # configure app using the Config class defined in config.py
    if os.environ.get("FLASK_ENV") == "development":
        app.config.from_object('config.DevelopmentConfig')
    else:
        app.config.from_object('config.ProductionConfig')

    with app.app_context():

        from home.home import home_bp
        app.register_blueprint(home_bp)

        from api.api import api_bp
        app.register_blueprint(api_bp)

        return app
