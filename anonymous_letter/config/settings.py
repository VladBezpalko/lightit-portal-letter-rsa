import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
SECRET_KEY = '*x1f9%!$$i40*3@h(-33w#rz64uztz#99*9tq05)!s%br4y4^w'

DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'django_filters',
    'corsheaders',

    'letter',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

BOSS_PUBKEY = """-----BEGIN PGP PUBLIC KEY BLOCK-----
Version: GnuPG v1

mQENBFlMQ1IBCADQ1TiMFOj1k3+bKZeKyVkQKrhkcJqcdM/l2k+mKhMf0oRGDwz+
pO7LTn5DsODxfbkxj+5Ev4MWU+wPw/XHw/6wBy8sVIj+PglmhDnkb9ahABXyksHt
1qT4CaZJ9URssZtRsNjKdGlolP4sxp40B1dQzwkYqkeNx5OFchrLtiRmcAM0KABJ
oprl8iMkYj6CUFgZUGO+lzMMmu1IfY5e/z+ptHeH+Z8J8+f1rVuGz3BhN9Vn4Zw2
qK3pnhsS73jZUNjB0/aDY6Ddut4BYmiOr1J+kgB3lFGkwRYrkBNamm4lSdMkXw6u
Ix/YsgbO8w4yIdbKJAXW65j2TUZvdVE5oEnVABEBAAG0F2FhYWFhYWEgPGFhYWFh
QGFhYWEuYWE+iQE4BBMBAgAiBQJZTENSAhsDBgsJCAcDAgYVCAIJCgsEFgIDAQIe
AQIXgAAKCRCZmXdM2YquHrqjCACaFj9wFHmyz7ReJBHhi7GtvWQ40GinIpgHMaGf
LWZK+06pee2zydpyW3m6OlHouQ1mOYLIxRqlARRosevblidq6hSdznwbOCVAs9GV
D228T5xEftFiInbq70iyj/fCRujdIIgG4QvAgRdkboUlyEPMWwZGuiehFVhTVReZ
DnqTsD0QVP5Sk1nesfZNRhwTjGPfEu0Tv+3uaBk11N8hUsw83GVwSMjymd9zdBNN
BfGOBYUWCW4NE9D5qcWKJWIxYOJvaisPmPeDv73cTlRmgiNKV/w2RnV5ZHqC0QdS
/N87TUiNwqsNTltB6ksKvp5lE7ycrkAYW7UjEUsjI0soCD8SuQENBFlMQ1IBCAC4
pbu7NC2/a/XY4bGfIYUUL7DJnHDAuiK33VuHl2kJqQEkpkRNq257N3GQeqDrhlsB
CcLZK81KWEC0Ftkk0VIgKprsN6RnwBsDTFEiFgOqyZsUgfy1ngYHIwQf+rgfuguR
lgt60vx4t//J41NIMka9m6F8PhyJNFovixqEwt6WowTsbIoYfBteMGiCvnTtmZyH
J3V4hgkMJ1w6HJp9oOGFa6Eoo6EEzNLge9ILpnJyBPrhuc8m0mDAX92vlVrwcXJb
Izb9dMtChO+krfwAg3jD2K8GEmCiPC4bvaX/78UG10AdfRu8K1Mu5S+ntqYD+UNa
v6D9u+P4PVj4Ak0gQAJTABEBAAGJAR8EGAECAAkFAllMQ1ICGwwACgkQmZl3TNmK
rh4b9wf+KrjuyT0g05oGIVC//eJSvgxosxE4fgW8qKz/o0uxZ9nYN3jp+hBrcwid
Szi2F6gCeQnrLJ3m4MygLCtUAhvHWkJF/vcelHUmSEq4wxdaeXLyLCoBn5aDv4ae
D4UxGvY3CYvgwmMeP60CaDvLjNMn2J5QRzFuC0QsLQ1/3fglkQ3W4JJwqJIWFvn+
eB6bRN4nH8U6qAknd6tDMmpRpIHMCv0jfdzKmzZ9nje+FSvytNgEXT23coCJi3nZ
qBKrrwPmY95hh+adOacnzw0XFDgqW4Rn4zyDacnrFyf6XO7U/W4dYVa/m9CtK1zM
rEGihydkp2bM60m7QrfdUwAyT4EqYQ==
=Hmq2
-----END PGP PUBLIC KEY BLOCK-----"""
