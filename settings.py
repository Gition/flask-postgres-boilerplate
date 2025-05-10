import os
"""
FLASK_APP = os.environ["FLASK_APP"]
FLASK_ENV = os.environ["FLASK_ENV"]
SECRET_KEY = os.environ["SECRET_KEY"]
DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DATABASE_NAME = os.environ["DATABASE_NAME"]
"""
FLASK_APP = os.getenv("FLASK_APP", "wsgi.py")
FLASK_ENV = os.getenv("FLASK_ENV", "production")
#SECRET_KEY = os.getenv("SECRET_KEY", "TsdfLs4@#$%08@#$89dJdFh5")
#DATABASE_NAME = os.getenv("DATABASE_NAME", "postgres")  # default database name
#DB_USERNAME = os.getenv("DB_USERNAME", "postgres")
#DB_PASSWORD = os.getenv("DB_PASSWORD", "my2#!@#initPass")
DB_HOST = os.getenv("DB_HOST", "localhost")
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_DATABASE_URI = (
    f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:5432/{DATABASE_NAME}"
)
