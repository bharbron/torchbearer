from flask import flask

import logging
import logging.config

app = Flask(__name__)
config_path = os.environ.get("TORCHBEARER_CONFIG_PATH", "torchbearer.config.DevelopmentConfig")
app.config.from_object(config_path)

with open(app.config["LOGCONFIG_PATH"], 'r') as f:
  logconfig = json.load(f)
logging.config.dictConfig(logconfig)
app.logger.info(u"Running with CONFIG_PATH: {}".format(config_path))

from . import views

from .database import db
app.logger.debug("Creating all metadata for flask_sqlalchemy")
db.create_all()