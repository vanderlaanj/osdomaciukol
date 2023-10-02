import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = '\2\1thisismyscretkey\1\2\e\y\y\h'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' },
    { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }]

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#SQLALCHEMY_DATABASE_URI = 'mysql://myapp@localhost/myapp'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# administrator list
ADMINS = ['you@example.com']

# pagination
POSTS_PER_PAGE = 3
MAX_SEARCH_RESULTS = 50

BABEL_DEFAULT_LOCALE = 'en'

LANGUAGES = {
    'en': {'flag':'gb', 'name':'English'},
    'pt': {'flag':'pt', 'name':'Portugal'}
}



#------------------------------
# GLOBALS FOR GENERAL APP's
#------------------------------
UPLOAD_FOLDER = basedir + '/app/static/uploads/'
IMG_UPLOAD_FOLDER = basedir + '/app/static/uploads/'
IMG_UPLOAD_URL = '/static/uploads/'
AUTH_TYPE = 1
AUTH_ROLE_ADMIN = 'Admin'
AUTH_ROLE_PUBLIC = 'Public'
APP_NAME = "My App 0.2"
APP_THEME = ""                  # default
#APP_THEME = "cerulean.css"      # COOL
#APP_THEME = "amelia.css"
#APP_THEME = "cosmo.css"
#APP_THEME = "cyborg.css"       # COOL
#APP_THEME = "flatly.css"
#APP_THEME = "journal.css"
#APP_THEME = "readable.css"
#APP_THEME = "simplex.css"
#APP_THEME = "slate.css"          # COOL
#APP_THEME = "spacelab.css"      # NICE
#APP_THEME = "united.css"
