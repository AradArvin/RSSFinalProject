

Configuration
-------------
In order to get the installed apps and packages work, some of the settings in the settings.py file in the project config folder
had to be changed. 
you can see the changes below:

Initialise environment variables:

..  code-block:: python

    from dotenv import load_dotenv
    load_dotenv()


Build paths inside the project like this: BASE_DIR / 'subdir'.

..  code-block:: python

    BASE_DIR = Path(__file__).resolve().parent.parent


Database: (with environ settings in .env file)

..  code-block:: python

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("DATABASE_NAME"),
            "USER": os.environ.get("DATABASE_USER"),
            "PASSWORD": os.environ.get("DATABASE_PASSWORD"),
            "HOST": os.environ.get("DATABASE_HOST"),
            "PORT": os.environ.get("DATABASE_PORT"),
        }
    }


Database For Tests:

..  code-block:: python

    if "test" in sys.argv:
        for db_test in ["default"]:  # Add other DBs if needed
            DATABASES[db_test]["ENGINE"] = "django.db.backends.sqlite3"
            if "--keepdb" in sys.argv:
                DATABASES[db_test]["TEST"]["NAME"] = (
                    "/dev/shm/" + db_test + ".test.db.sqlite3"
                )


Timezone:

..  code-block:: python

    TIME_ZONE = "Asia/Tehran"

    USE_I18N = True

    USE_TZ = True


Static files:

..  code-block:: python

    STATIC_URL = "static/"
    STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]


Media Files:

..  code-block:: python

    MEDIA_URL = "media/"
    MEDIA_ROOT = BASE_DIR / "media"


AUTHENTICATION:

..  code-block:: python

    AUTH_USER_MODEL = "staff.CustomUserModel"

    AUTHENTICATION_BACKENDS = [
        "django.contrib.auth.backends.ModelBackend",
        "staff.backends.CustomUserBackend",
    ]


DEBUG_TOOLBAR:

..  code-block:: python

    THIRDPARTY_APPS = [
        'debug_toolbar',
    ]
    MIDDLEWARE = ['debug_toolbar.middleware.DebugToolbarMiddleware']
    INTERNAL_IPS = [
        "127.0.0.1",
    ]





**These settings are needed to run the project without errors**