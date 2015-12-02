import os

from .settings import *


empty = object()


def environ(key, default=empty):
    try:
        return os.environ[key]
    except KeyError:
        if default is not empty:
            return default
        raise Exception("missing {} from environment".format(key))


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ["*"]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django.request": {
            "handlers": ["console"],
            "level": "INFO",
            "propagate": True
        }
    }
}

import dj_database_url
DATABASES = {
    "default": dj_database_url.config(default="postgres://localhost/yourdb")
}

LIBCLOUD_PROVIDERS = {
    "default": {
        "type": "libcloud.storage.types.Provider.GOOGLE_STORAGE",
        "user": environ("GCS_KEY"),
        "key": environ("GCS_SECRET"),
        "bucket": "pachyderm_publishing",
    },
}

DEFAULT_FILE_STORAGE = "storages.backends.apache_libcloud.LibCloudStorage"
