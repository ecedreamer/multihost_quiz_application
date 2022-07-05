from decouple import config

DEBUG = config("DEBUG", default=False, cast=bool)


if DEBUG:
    from .dev_settings import *
else:
    from .live_settings import *