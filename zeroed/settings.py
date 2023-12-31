"""
Django settings for zeroed project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from pathlib import Path
import os
import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

env = environ.Env()
environ.Env.read_env()
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1',]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'feed.apps.FeedConfig',
    'django_truncate',
    'bootstrap5',
    'password_reset',
    'django_quill',
    'django_bleach',
    'django_cleanup.apps.CleanupConfig',
    'django_unused_media',
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

ROOT_URLCONF = 'zeroed.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
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

WSGI_APPLICATION = 'zeroed.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/'

DEFAULT_FROM_EMAIL = env('EMAIL_HOST_USER')
EMAIL_BACKEND = 'django_ses.SESBackend'
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_SESSION_TOKEN = env('AWS_SESSION_TOKEN')
# settings for bleach
# Which HTML tags are allowed
BLEACH_ALLOWED_TAGS = [
    "address", "article", "aside", "footer", "header", "h1", "h2", "h3", "h4",
    "h5", "h6", "hgroup", "main", "nav", "section", "blockquote", "dd", "div",
    "dl", "dt", "figcaption", "figure", "hr", "li", "main", "ol", "p", "pre",
    "ul", "a", "abbr", "b", "bdi", "bdo", "br", "cite", "code", "data", "dfn",
    "em", "i", "kbd", "mark", "q", "rb", "rp", "rt", "rtc", "ruby", "s", "samp",
    "small", "span", "strong", "sub", "sup", "time", "u", "var", "wbr", "caption",
    "col", "colgroup", "table", "tbody", "td", "tfoot", "th", "thead", "tr", "img"
]
# Which HTML attributes are allowed
BLEACH_ALLOWED_ATTRIBUTES = [
    'abbr', 'accept', 'accept-charset', 'accesskey', 'action',
    'allow', 'alt', 'as', 'autocapitalize', 'autocomplete',
    'blocking', 'charset', 'cite', 'class', 'color', 'cols',
    'colspan', 'content', 'contenteditable', 'coords', 'crossorigin',
    'data', 'datetime', 'decoding', 'dir', 'dirname', 'download',
    'draggable', 'enctype', 'enterkeyhint', 'fetchpriority', 'for',
    'form', 'formaction', 'formenctype', 'formmethod', 'formtarget',
    'headers', 'height', 'hidden', 'high', 'href', 'hreflang',
    'http-equiv', 'id', 'imagesizes', 'imagesrcset', 'inputmode',
    'integrity', 'is', 'itemid', 'itemprop', 'itemref', 'itemtype',
    'kind', 'label', 'lang', 'list', 'loading', 'low', 'max',
    'maxlength', 'media', 'method', 'min', 'minlength', 'name',
    'nonce', 'optimum', 'pattern', 'ping', 'placeholder', 'popover',
    'popovertarget', 'popovertargetaction', 'poster', 'preload',
    'referrerpolicy', 'rel', 'rows', 'rowspan', 'sandbox', 'scope',
    'shape', 'size', 'sizes', 'slot', 'span', 'spellcheck', 'src',
    'srcdoc', 'srclang', 'srcset', 'start', 'step', 'style',
    'tabindex', 'target', 'title', 'translate', 'type', 'usemap',
    'value', 'width', 'wrap',
]
# Which CSS properties are allowed in 'style' attributes
BLEACH_ALLOWED_STYLES = [
    'font-family', 'font-weight', 'text-decoration', 'font-variant', 'color'
]
# Which protocols (and pseudo-protocols) are allowed in 'src' attributes
# (assuming src is an allowed attribute)
BLEACH_ALLOWED_PROTOCOLS = [
    'http', 'https', 'data'
]
# Strip unknown tags if True, replace with HTML escaped characters if False
BLEACH_STRIP_TAGS = False

# Strip HTML comments, or leave them in.
BLEACH_STRIP_COMMENTS = True
