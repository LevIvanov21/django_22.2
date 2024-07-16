from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@ya.ru',
            first_name='admin',
            last_name='ya.ru',
            is_staff=True,
            is_superuser=True
        )
        user.set_password('123qwe456rty')
        user.save()