class DevelopmentConfig(object):
  SQLALCHEMY_DATABASE_URI = "sqlite:///torchbearer.db"
  DEBUG = True
  SECRET_KEY = os.environ.get("TORCHBEARER_CHARGEN_SECRET_KEY", "landpleasantandreda")
  LOGCONFIG_PATH = "torchbearer/logconfig.dev.json"