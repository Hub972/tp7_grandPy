import os
#data base > postgresql-spherical-83284
G_KEY = 'AIzaSyC4CNHOq10NKaPV_IpyHlLCYnZBraLKSGI'
BING_KEY = 'AkuEXWHCBJkoeCzvttohvxa8Q4aVaGlvbrLfbZfb9z6Hxs-GqmAVeO0Ua9kaTGUx'
# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
SECRET_KEY = "!&hjeVc=S'V'o{$0'_B#E b?<"

# Database initialization
if os.environ.get('DATABASE_URL') is None:
    pass
else:
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


