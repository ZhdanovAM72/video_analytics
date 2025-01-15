from pathlib import Path
import os
# import tempfile

# from django.conf import settings
from django.urls import reverse_lazy
from dotenv import load_dotenv

load_dotenv()

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY', default='django_video')

# ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', default='*').split(', ')
ALLOWED_HOSTS = ('*', '127.0.0.1')

# DEBUG = os.getenv('DEBUG') == 'True'
DEBUG = 'True'

INSTALLED_APPS = [
    'video.apps.VideoConfig',
    'users.apps.UsersConfig',
    'core.apps.CoreConfig',
    'about.apps.AboutConfig',
    'check_list.apps.CheckListConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sorl.thumbnail',
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

ROOT_URLCONF = 'video_analytics.urls'

# TEMPLATES_DIR = BASE_DIR / 'templates'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'core.context_processors.year.year',
            ],
        },
    },
]

WSGI_APPLICATION = 'video_analytics.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('POSTGRES_DB', default='django'),
#         'USER': os.getenv('POSTGRES_USER', default='django'),
#         'PASSWORD': os.getenv('POSTGRES_PASSWORD', default='postgre'),
#         'HOST': os.getenv('DB_HOST', default='db'),
#         'PORT': os.getenv('DB_PORT', default=5432)
#     }
# }

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

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# MEDIA_DIRS = [
#     os.path.join(BASE_DIR, 'media')
# ]
# TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.BASE_DIR)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CORS_ORIGIN_ALLOW_ALL = True
CORS_URLS_REGEX = r'^/api/.*$'

CSRF_TRUSTED_ORIGINS = ['https://*.bobsik.ru/', 'http://*.bobsik.ru/', 'http://127.0.0.1*']

LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'video:index'
# LOGOUT_REDIRECT_URL = 'users:logout'
LOGOUT_URL = reverse_lazy('logout')
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, 'sent_emails')

# Max value settings for core models
MAX_CHARFIELD_LENGTH = 200
MAX_STR_MODEL_LENGTH = 15

# Max value settings for user models
MAX_EMAILFIELD_USER_LENGTH = 254
MAX_CHARFIELD_USER_LENGTH = 150
MAX_STR_USER_MODEL_LENGTH = 25

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}

VIDEO_PER_PAGE = 6

THUMBNAIL_DEBUG = True
