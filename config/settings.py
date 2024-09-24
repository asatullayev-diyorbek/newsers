from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-titgo_-a*7_chjz*%d_4$r3by(=f4es@-znxkv#9)c7)c^@m#_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'newsers',
    'register',

    # Ckeditor
    'ckeditor',
    'ckeditor_uploader',

    'django_cleanup.apps.CleanupConfig',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.joinpath('templates')],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [

]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR.joinpath('staticfiles')
STATICFILES_DIRS = [
    BASE_DIR.joinpath('static'),
]
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'


MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR /'media'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'login'

# email
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'asatullayevblog@gmail.com'
EMAIL_HOST_PASSWORD = 'ztuqrinhdhyzebux'
DEFAULT_FROM_EMAIL = 'asatullayevblog@gmail.com'


# Ckeditor
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': [
            {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': ['Cut', 'Copy', 'Paste', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': ['Find', 'Replace', '-', 'SelectAll', '-', 'Scayt']},
            {'name': 'basicstyles', 'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph', 'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-', 'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert', 'items': ['Image', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            {'name': 'styles', 'items': ['Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['Maximize', 'ShowBlocks']},
        ],
        'height': 500,
        'width': 'auto',
        'extraAllowedContent': '*[*]',
        'extraPlugins': 'iframe',
    },
}

CKEDITOR_UPLOAD_PATH = "media/ckeditor/"
CKEDITOR_RESTRICT_BY_USER = True


# Jazzmin
JAZZMIN_SETTINGS = {
    "site_title": "Newsers",
    "welcome_sign": "Admin Paneliga Xush Kelibsiz!",
    "copyright": "2024 Sizning Nomingiz",
    "search_model": "auth.User",
    "user_avatar": "images/user_avatar.png",
    "topmenu_links": [
        {"name": "Bosh Sahifa", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "Yangiliklar", "url": "/admin/newsers/news/", "permissions": ["app_name.view_model"]},
    ],
    "usermenu_links": [
        {"model": "auth.User"},
        {"model": "auth.Group"},
    ],
    "show_sidebar": True,
    "show_ui_builder": True,
    "changeform_format": "horizontal",
    "pagination": 20,
}