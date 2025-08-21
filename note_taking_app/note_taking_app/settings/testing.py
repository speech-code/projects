from .base import *

DEBUG = False

ALLOWED_HOSTS = []

# Use a different database for testing, e.g., in-memory SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}
