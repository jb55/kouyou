import logging
import os.path

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s %(levelname)s %(message)s',
)

# Django settings for jgblue project.
PROJECT_DIR = "/home/jb55/kouyou/"
STATIC_DIR = os.path.join(PROJECT_DIR, "static")
TEMPLATES_DIR = os.path.join(PROJECT_DIR, "templates")

DEBUG = True
TEMPLATE_DEBUG = DEBUG

# Email
SERVER_EMAIL = "django@newchan.org"

ADMINS = (
    ('Admins', 'admin@newchan.org'),
)

MANAGERS = ADMINS

# memcached
#CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
#CACHE_MIDDLEWARE_KEY_PREFIX = 'kouyou'
#CACHE_MIDDLEWARE_SECONDS = 10 # 10 seconds, pretty much near real time

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
MEDIA_ROOT = STATIC_DIR

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = 'http://static.newchan.org/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = 'http://static.newchan.org/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'ea0gdtmdh4(78!o=qcq7o+!um*$1*1%4&+%*x7d#wm=5s@_r89'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
#    'django.middleware.cache.UpdateCacheMiddleware', # must be first
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'jgblue.middleware.StripWhitespaceMiddleware', 
#    'django.middleware.cache.FetchFromCacheMiddleware', # must be last
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
)

ROOT_URLCONF = 'kouyou.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    TEMPLATES_DIR,
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'kouyou.boards',
)
