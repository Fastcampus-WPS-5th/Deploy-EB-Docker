# deploy.py
from .base import *

config_secret_deploy = json.loads(open(CONFIG_SECRET_DEPLOY_FILE).read())

# WSGI application
WSGI_APPLICATION = 'config.wsgi.deploy.application'

# Static URLs
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

# 배포모드니까 DEBUG는 False
DEBUG = True
ALLOWED_HOSTS = config_secret_deploy['django']['allowed_hosts']

# Database
DATABASES = config_secret_deploy['django']['databases']

print('@@@@@@ DEBUG:', DEBUG)
print('@@@@@@ ALLOWED_HOSTS:', ALLOWED_HOSTS)


# 1. RDS연동 후 데이터 들어가는지 확인
#    DJANGO_SETTINGS_MODULE=config.settings.deploy설정
#    createsuperuser커맨드 실행 후 pgAdmin으로 auth_user테이블에 데이터가 들어갔는지 확인
