import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')

    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')

      # --- SOLO PARA DEBUG EN RENDER ---
    print("== VARIABLES DE ENTORNO LEÍDAS ==")
    print("SECRET_KEY:", os.environ.get('SECRET_KEY'))
    print("SQLALCHEMY_DATABASE_URI:", os.environ.get('SQLALCHEMY_DATABASE_URI'))
    print("EMAIL_USER:", os.environ.get('EMAIL_USER'))
    print("EMAIL_PASS:", os.environ.get('EMAIL_PASS'))
    print("================================")

