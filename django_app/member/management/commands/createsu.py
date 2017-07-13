import json

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management import BaseCommand

User = get_user_model()


class Command(BaseCommand):
    def handle(self, *args, **options):
        # CONFIG_SECRET_COMMON_FILE (.config_secret/settings_common.json)을 읽어옴
        config_secret_common = json.loads(open(settings.CONFIG_SECRET_COMMON_FILE).read())
        username = config_secret_common['django']['default_superuser']['username']
        password = config_secret_common['django']['default_superuser']['password']
        # 만약 username에 해당하는 User가 없을 경우
        if not User.objects.filter(username=username).exists():
            # 해당 username으로 superuser를 생성
            User.objects.create_superuser(
                username=username,
                password=password,
                email=''
            )
            print('Superuser %s created' % username)
        else:
            print('Superuser %s is already exist' % username)
