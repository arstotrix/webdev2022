import os


class Config:
    MONGODB_USERNAME = os.environ.get('MONGODB_USERNAME', "flask_user")
    MONGODB_PASSWORD = os.environ.get('MONGODB_PASSWORD', "flask_password")
    MONGODB_HOSTNAME = os.environ.get('MONGODB_HOSTNAME', "mongodb")
    MONGODB_DATABASE = os.environ.get('MONGODB_DATABASE', "flask_db")

    MONGO_URI = (
        'mongodb://' + 
        MONGODB_USERNAME + ':' + 
        MONGODB_PASSWORD + '@' + 
        MONGODB_HOSTNAME + ':27017/' + 
        MONGODB_DATABASE
    )
