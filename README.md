## PASSO A PASSO PARA INSTALAR E USAR###

Projeto REST###
https://www.django-rest-framework.org/#installation

Como funciona rotas > view > model > serializer

Primeiro passos
#Instala o ambiente
python -m venv ./fcs

# ativa
bin/activate

pip install Django
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support

#Inicia Django e projeto exemplo api
django-admin startproject model_site xpto

acessar o api
cd .\api\

#cria o app
python manage.py startapp core   # Qualquer nome exemplo core

registra em settings.apy nos INSTALLED_APPS = [
'core',

# criar banco de dados
python manage.py migrate

# criar super usuario
python manage.py createsuperuser
User: 
Senha: 

#rodar projeto
python manage.py runserver

http://127.0.0.1:8000/

# para acessar admin
http://127.0.0.1:8000/admin
admim

http://127.0.0.1:8000/cliente

# criar os dados
models.py
# apos criar os dados
python manage.py makemigrations

#apos criar ou alterar repete o  ## 

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver


url.py

from django.contrib import admin
from django.urls import path, include
from core.views import ClienteViewSet
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]

----------------------------------------------
settings.py

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-sw@dflw$_pl=p1+w$3t4kcb@7*-yy43&v^urmqf(x44gi(9g6^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
    'rest_framework',
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

ROOT_URLCONF = 'api.urls'

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

WSGI_APPLICATION = 'api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
---------------------
[CORE]

Serializers.py

rom rest_framework import serializers
from .models import Cliente


# Serializers define the API representation.
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf', 'data_nascimento', 'sexo', 'email', 'telefone', 'endereco', 'bairro', 'cidade', 'estado', 'cep']
        
        
------------------
models.py
from django.db import models

class Cliente(models.Model):
    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
        ("O", "Outros")
    )
    nome = models.CharField(max_length=60, null=False, blank=False)
    cpf = models.CharField(max_length=12, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    #sexo = models.CharField(max_length=2)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)
    email = models.EmailField(null=False, blank=False)
    telefone = models.CharField(max_length=14, blank=False)
    endereco = models.CharField(max_length=50, blank=True)
    bairro = models.CharField(max_length=40, blank=True)
    cidade = models.CharField(max_length=40, blank=True )
    estado = models.CharField(max_length=3, blank=True)
    cep = models.CharField(max_length=9, blank=True)
    
      
    
    def __str__(self):
        return self.nome
    
    


