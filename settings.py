import os

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Priscila Manhaes', 'pmnhaes@gmail.com'),
    # ('Ruhan Ferreira Almeida', 'ruhanfa@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT_PATH, 'financeiro.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        }
}

TIME_ZONE = 'America/Sao_Paulo'
LANGUAGE_CODE = 'pt-br'

SITE_ID = 1
USE_I18N = True
USE_L10N = True

MEDIA_ROOT = os.path.join(PROJECT_ROOT_PATH, 'media')
MEDIA_URL = '/media'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'p#rm2q#-pn)+%y=l=o(6py1rf%2p@cm*$1y1950rnl6n6qcstl'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT_PATH, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
#    'django.contrib.staticfiles',
    'api',
    'empenho',
)


