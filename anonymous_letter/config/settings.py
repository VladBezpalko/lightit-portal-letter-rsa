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

BOSS_PUBKEY = """MIIEIjANBgkqhkiG9w0BAQEFAAOCBA8AMIIECgKCBAEAo9c8WlERqorcGALtWrCP
GpVoE0UCtyprVZubf4U0wEw7CEjRejdahi6+7owiXPmIDz3py1ZVJACDeD8A5Xg9
YuQPKv2o/LIrN5vW9yyYTUagMs0JZTDRfGjhcMrTiZYxTamKv1WyCDThPPj58JXm
kdE55RWmkMFy9QFp/0HhUSXWEVAIN1kRK44uwpz1EEfP7KZOlh/SY7LRHcRFW8UR
sAvin+AqbchOpmd6+fQdpV+m54ZpIjgClZaRC3hugGL1+0ALT6SIfXiw79IN38ne
xLw1n9enymhgEn4oppDv0cQFG6vnx0ZZg5j5AUuv2HNwl/GZJHrbpuROXpZZFtmp
j8jNcL8vn1dUJTBjk/S2hSAVBXqIbskerSNSObzid2H1LLT4/u1ZF3X/hsDdFwpG
8xWf7CSlACjW7MgNN/aXBIpdhpmtmDSGSFIogDx+2akwbseb14d0F6kG4RMemSzG
Y62Xr/TvZyanYoQDzG+SQxfNmPvMC6DlTMt4TRPp0lUUUWj/ez6c16XyRFpmsP1n
BXSePsxLmEoH4qlV9Ct52CURJZ7g4ICIj3vrwUUeOIAL3nhXMJAG3mGUp3JDVcS+
xUWC/Ri7g/zPz1GtBWirsd8lo3XZ14UfPgXtqzlcRVI/5JuH1mlRiNbvmOBrvLCo
R/vQfiTBBLVzqpAhvyFz7JwgDgRUmZOocyjn1LwLiyxfH1Z2DrBTugy/ZVeKuuFX
ve7cujPqIUXkTZ8L50DcMD7J7u7RerhIRgCtcAJnxt4V3nMDtoC+VjUaiMjw/e+M
WZdOqA+Rerl7Bwmj0vA36/9l1OXON7BGFIgM/XjiUB8sIVrCLh81AO0ojPDo3e9L
IpsoODVW40ASac7kx4l3NeRdzPY4YFOzoJwdb+E7JFErT2jgVYj4bvEAZvEM6wuT
bX1DA5/OE21IsTItjfCzb+SYBHF3WYGbRPdiZa8FyYZAaGLPfpezmYVxTnXLUHyS
CKukyMKHj5BCAkWP3LDTLLYIY9MyrEOpF4cBHeAJm4WO05Oe7mj9w+kq82Sgpr4K
tvPSXsG7ieEg4kd2pwUXR+ln579O+z5GQb+Ivky0tyPgCcGXGRpe7vn39ETQpp7K
Fi+42eEpQ6ej5tUM0ctWgvRWaGeSRjQfd4keMVEkq/ErvhkY1Qx8JWaxwnFY+W3b
v8GgvsQdsUd40fSFjDXtlKEFgcaEv4cf2bq3O6Bp7eu2/TyprYMCi8E7uNvTe6hS
m8pbPaYO3UZF5RcPt0rEY3tAthCagEPvLAIyAAdPB7RUftnwIXJ6bbCAKA6dnmHu
ldevj2ZNcQQcxtGN/fbBxTkPV2IHE9lbXqaMw9NXUzSWv9pcZVt1ZUJpDFHYydGo
hwIDAQAB"""
