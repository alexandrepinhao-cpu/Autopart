import os

class Config:
    # General application config
    DEBUG = False
    TESTING = False
    ENV = 'production'

    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Security settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')

    # Other configuration settings can go here

# Development configuration
class DevelopmentConfig(Config):
    DEBUG = True
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_DEV')

# Testing configuration
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL_TEST')

# Production configuration
class ProductionConfig(Config):
    pass
