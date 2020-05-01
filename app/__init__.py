from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app.ui import bp as ui_bp
from app.api import bp as api_bp

app.register_blueprint(ui_bp, url_prefix='/')
app.register_blueprint(api_bp, url_prefix='/api')

