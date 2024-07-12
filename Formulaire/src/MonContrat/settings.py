import os.path
from pathlib import Path

# création des liens au sein du projet
BASE_DIR = Path(__file__).resolve().parent.parent


# Données nécessaires à l'utilisation du localhost de Django
SECRET_KEY = 'django-insecure-=d_m=68j(zos@y2u0yz5yfswjob3y#iw8j!*bsp#=w)0y70&_k'
DEBUG = True
ALLOWED_HOSTS = []


# Définition des applications
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Formulaire',
    'BaseDonnee',
    'bootstrap5'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# chemin des urls
ROOT_URLCONF = 'MonContrat.urls'

# chemins des fichiers CSS et JavaScript
STATICFILES_DIRS = [
    BASE_DIR / "static"
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'MonContrat/templates')], # création des chemins entre les pages html
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

            ],
        },
    },
]

WSGI_APPLICATION = 'MonContrat.wsgi.application'


# Base de données
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# définition d'une clef par défaut pour la base de données
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# validation de mot de passe
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalisation

LANGUAGE_CODE = 'fr-FR' # français

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# urls des fichiers statiques (css, JavaScript, Images)
STATIC_URL = 'static/'