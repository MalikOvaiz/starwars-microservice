import os
from app import app


class Config:
    """SECRET_KEY
    Use this class to share any default attributes with any subsequent
    classes that inherit from Config.
    """
    DEBUG = False
    TESTING = False

    # Only required when using the session object
    # Generated with secrets.token_urlsafe(16)
    # You could also use os.urandom(16)
    SECRET_KEY = "11Fnw8U6DXrMFvbH9jCdZQ"

    SWAGGER_CONF = {
        "headers": [
        ],
        "specs": [
            {
                "endpoint": 'apispec_1',
                "route": '/apispec_1.json',
                "rule_filter": lambda rule: True,  # all in
                "model_filter": lambda tag: True,  # all in
            }
        ],
        "static_url_path": "/flasgger_static",
        # "static_folder": "static",  # must be set by user
        "swagger_ui": True,
        "specs_route": "/apidocs/",
        'title': 'DSS API Documentation'
    }

    SWAGGER_TEMPLATE = {
        "swagger": "2.0",
        "info": {
            "title": "Star War Movies -  Microservice",
            "description": "Interview Exam",
            "contact": {
                "responsibleOrganization": "TU Clausthal",
                "responsibleDeveloper": "Awais Mushtaq",
                "email": "ovaiz.mushtaq@gmail.com",
                "url": "https://ovaizmushtaq.wixsite.com/awaismushtaq",
            },
            "termsOfService": "https://ovaizmushtaq.wixsite.com/awaismushtaq",
            "version": "0.0.1"
        },

        # comment for local environment
        # "host": "www.example.com",  # overrides localhost:500
        # "basePath": "/",  # base bash for blueprint registration
        # "schemes": 'https',
        "operationId": "getmyData"
    }


class ProductionConfig(Config):
    """
    This class will inherit any attributes from the parent Config class.
    Use this class to define production configuration atrributes, such
    as database usernames, passwords, server specific files & directories etc.
    """
    CACHE_API = 0
    STORAGE_DIRECTORY = os.path.join(app.root_path, "storage")


class DevelopmentConfig(Config):
    """
    This class will inherit any attributes from the parent Config class.
    Use this class to define development configuration atrributes, such
    as local database usernames, passwords, local specific files & directories etc.
    """
    DEBUG = True
    CACHE_API = 0
    STORAGE_DIRECTORY = os.path.join(app.root_path, "storage")
