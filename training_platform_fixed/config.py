import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'clave-secreta'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///training.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False