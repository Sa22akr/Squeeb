from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'accounts'

    def ready(self):
        import os
        from django.contrib.auth import get_user_model
        from django.db.utils import OperationalError, ProgrammingError

        if os.environ.get("CREATE_SUPERUSER") == "True":
            try:
                User = get_user_model()
                username = os.environ.get("DJANGO_SUPERUSER_USERNAME")
                email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
                password = os.environ.get("DJANGO_SUPERUSER_PASSWORD")

                if username and password:
                    user, created = User.objects.get_or_create(username=username)
                    user.email = email
                    user.is_staff = True
                    user.is_superuser = True
                    user.set_password(password)
                    user.save()

            except (OperationalError, ProgrammingError):
                pass