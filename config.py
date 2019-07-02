import os
#data base > postgresql-spherical-83284


# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])


# Database initialization
if os.environ.get('DATABASE_URL') is None:
    pass
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
if os.environ.get('G_KEY') is None:
    raise Exception("A System variable named 'G_key' is required.")
else:
    G_KEY = os.environ.get('G_KEY')

if os.environ.get('BING_KEY') is None:
    raise Exception("A System variable named 'BING_KEY' is required.")
else:
    BING_KEY = os.environ.get('BING_KEY')

if os.environ.get('FLASK_SECRET_KEY') is None:

    raise Exception("A System variable named 'SECRET_KEY' is required.")
else:
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')


