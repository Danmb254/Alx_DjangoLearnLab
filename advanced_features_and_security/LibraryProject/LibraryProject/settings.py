"""
Django settings for advanced_features_and_security project.

Security-focused settings included for:
- CSRF protection
- XSS prevention
- SQL injection safety (via ORM)
- HTTPS enforcement
"""

import os
from pathlib import Path

# -----------------------------------------
# Base Directory
# -----------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# -----------------------------------------
# SECURITY SETTINGS
# -----------------------------------------
DEBUG = False  # Must be False in production

ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Add your production host here

# Secret key (ALX may provide one)
SECRET_KEY = 'your-secret-key-here'  # Replace with a secure key in production

# -----------------------------------------
# Installed Applications
# -----------------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Local apps
    'bookshelf',
]

# -----------------------------------------
# Middleware
# -----------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',  # CSRF protection
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # Clickjacking protection
]

ROOT_URLCONF = 'LibraryProject.urls'

# -----------------------------------------
# Templates
# -----------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'bookshelf', 'templates')],
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

WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# -----------------------------------------
# Database (SQLite for ALX)
# -----------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -----------------------------------------
# Password Validators
# -----------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -----------------------------------------
# Internationalization
# -----------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -----------------------------------------
# Static Files
# -----------------------------------------
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# -----------------------------------------
# DEFAULT AUTO FIELD
# -----------------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# -----------------------------------------
# -----------------------------------------
# SECURITY SETTINGS (Task 2 & 3)
# -----------------------------------------
# Force HTTPS
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Secure cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Clickjacking protection
X_FRAME_OPTIONS = 'DENY'

# Browser-side protections
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True