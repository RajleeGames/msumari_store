
import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


# ============================================================
# SECURITY
# ============================================================

SECRET_KEY = 'BHommlfCUzsShqBAsrxei3wKf7NKZ9IQofq7DVCGDUbbsnH82UbwcRSdoElTEirT'

DEBUG = True

ALLOWED_HOSTS = [
    'msumarijr.store',
    'www.msumarijr.store',
    '127.0.0.1',
    'localhost',
]


# Required for POST forms when using HTTPS/domain
CSRF_TRUSTED_ORIGINS = [
    'https://msumarijr.store',
    'https://www.msumarijr.store',
]


# Useful when Django is behind Nginx
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = False

SECURE_CONTENT_TYPE_NOSNIFF = True

X_FRAME_OPTIONS = 'DENY'

SECURE_REFERRER_POLICY = 'same-origin'


# ============================================================
# APPLICATIONS
# ============================================================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'core',
]


# ============================================================
# MIDDLEWARE
# ============================================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ============================================================
# URLS
# ============================================================

ROOT_URLCONF = 'config.urls'


# ============================================================
# TEMPLATES
# ============================================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            BASE_DIR / 'templates',
        ],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',

                'django.contrib.auth.context_processors.auth',

                'django.contrib.messages.context_processors.messages',

                'core.context_processors.shop_context',
            ],
        },
    },
]


# ============================================================
# WSGI
# ============================================================

WSGI_APPLICATION = 'config.wsgi.application'


# ============================================================
# DATABASE
# ============================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',

        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ============================================================
# PASSWORD VALIDATION
# ============================================================

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


# ============================================================
# LANGUAGE / TIME
# ============================================================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Dar_es_Salaam'

USE_I18N = True

USE_TZ = True


# ============================================================
# STATIC FILES
# ============================================================

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'


# ============================================================
# MEDIA FILES
# ============================================================

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'


# ============================================================
# AUTHENTICATION
# ============================================================

LOGIN_URL = 'login'

LOGIN_REDIRECT_URL = 'dashboard'

LOGOUT_REDIRECT_URL = 'login'


# ============================================================
# DJANGO DEFAULTS
# ============================================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# ============================================================
# FILE UPLOAD SAFETY
# ============================================================

FILE_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024

DATA_UPLOAD_MAX_MEMORY_SIZE = 15 * 1024 * 1024


# ============================================================
# SESSION
# ============================================================

SESSION_COOKIE_AGE = 60 * 60 * 12

SESSION_SAVE_EVERY_REQUEST = True


# ============================================================
# EMAIL
# ============================================================

# No email service configured yet.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# ============================================================
# QZ TRAY - DEVELOPMENT / PRODUCTION
# ============================================================

# DEVELOPMENT:
#
# Kibosho_central_amcos/
# ├── manage.py
# ├── qz_keys/
# │   ├── digital-certificate.txt
# │   └── private-key.pem
# └── static/
#     └── vendor/
#         └── qz/
#             └── qz-tray.js
#
# Production can override QZ_KEYS_DIR using environment variables.


QZ_KEYS_DIR = Path(
    os.getenv(
        "QZ_KEYS_DIR",
        str(BASE_DIR / "qz_keys")
    )
).expanduser().resolve()


QZ_CERT_PATH = Path(
    os.getenv(
        "QZ_CERT_PATH",
        str(
            QZ_KEYS_DIR /
            "digital-certificate.txt"
        )
    )
).expanduser().resolve()


QZ_PRIVATE_KEY_PATH = Path(
    os.getenv(
        "QZ_PRIVATE_KEY_PATH",
        str(
            QZ_KEYS_DIR /
            "private-key.pem"
        )
    )
).expanduser().resolve()


QZ_SIGNATURE_ALGORITHM = "SHA512"

QZ_MAX_SIGNING_BYTES = 1024 * 1024


# Leave empty during first test.
# The JavaScript will find the XPrinter automatically.
QZ_PRINTER_NAME = (
    os.getenv(
        "QZ_PRINTER_NAME",
        "XP-80C"
    ).strip()
)


# Development debug
if DEBUG:
    print(
        "[QZ] KEYS DIR:",
        QZ_KEYS_DIR
    )

    print(
        "[QZ] CERT:",
        QZ_CERT_PATH,
        "| exists:",
        QZ_CERT_PATH.exists()
    )

    print(
        "[QZ] PRIVATE KEY:",
        QZ_PRIVATE_KEY_PATH,
        "| exists:",
        QZ_PRIVATE_KEY_PATH.exists()
    )

    print(
        "[QZ] PRINTER:",
        QZ_PRINTER_NAME or "AUTO DETECT"
    )