from flask_sqlalchemy import SQLAlchemy
from torchbearer import app

app.logger.info("Initiating database with flask_sqlalchemy")
app.logger.info("Initiating database engine for torchbearer")
db = SQLAlchemy(app)