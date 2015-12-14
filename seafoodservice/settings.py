import os


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

GOOGLE_MAPS_SETTINGS = {
    'center_longitude': 10.0,
    'center_latitude': 41.0,
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'seafoodservice',
        'USER': 'postgres',
        'PASSWORD': '1',
        'HOST': '',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '',                      # Set to empty string for default.
    }
}

ALLOWED_HOSTS = []

TIME_ZONE = 'Europe/Minsk'


LANGUAGE_CODE = 'ru-ru'

gettext = lambda s: s
LANGUAGES = [
    ('ru', gettext('Russian')),
    ('en', gettext('English')),
]

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'
MODELTRANSLATION_FALLBACK_LANGUAGES = ('ru', 'en')
MODELTRANSLATION_LANGUAGES = ('en', 'ru')
MODELTRANSLATION_TRANSLATION_REGISTRY = 'translation'

MODELTRANSLATION_TRANSLATION_FILES = (
    'information.translation',
)

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = os.path.abspath('./media/')
MEDIA_PATH = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media/'))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = os.path.join(BASE_DIR, 'assets/')

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)




# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'i!pp-9*^*460o+t-!1z7tpl=t5c9l@7$9u@3e0)h-da@mgip@$'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'seafoodservice.urls'

WSGI_APPLICATION = 'seafoodservice.wsgi.application'

INSTALLED_APPS = (
    'pages',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'partners',
    'modeltranslation',
    'django.contrib.admin',
    'mptt',
    'gallery',
    'certificates',
    'information',
    'captcha',
    'contacts',
    'services',
    'transportation',
    'django_summernote',
    'south',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'pages/templates')]
ADMIN_TOOLS_MENU = 'menu.CustomMenu'
ADMIN_TOOLS_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'dashboard.CustomAppIndexDashboard'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
    'django.core.context_processors.i18n'
    )

CAPTCHA_OUTPUT_FORMAT = '%(text_field)s %(image)s %(hidden_field)s'

try:
    from local_settings import *
except ImportError:
    pass

SOUTH_MIGRATION_MODULES = {
    'captcha': 'captcha.south_migrations',
}

LOCALE_PATHS = (
    'locale',
)

# mail.ru
PASSWORD = "ServiceSeaFood"
EMAIL = "seafoodservice@inbox.ru"

#jivosite
SITEHELP_SETTINGS = {
"Connect using": "any xmpp/jabber client",
"Login": "seafoodservice@sitehelp.im",
"Password": "Seafoodservice4",
"Domain": "sitehelp.im",
"Port": 5222,
}
