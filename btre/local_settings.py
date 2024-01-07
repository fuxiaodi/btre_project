# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ubsq#xai!qa_!dsi=61a&mbqn)lxtl*x48$fi0v-l^k%0z1^bn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['45.55.200.14' ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'btre_prod',
        'USER': 'dbadmin',
        'PASSWORD': 'Fxd1986@',
        'HOST': 'localhost',
    }

}

# Email config
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER='fuxiaodi.amy@gmail.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
