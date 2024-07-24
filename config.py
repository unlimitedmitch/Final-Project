import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'D5JX0RR5GYLS2041YYRUBXDKFU8MAQPPD94H68N7'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/survey_database'