from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Custom Model For user(Author)


class CustomUser(AbstractUser):
    display_name = models.CharField(verbose_name=_("Display name"), max_length=30, help_text=_(
        "Will be shown e.g. when commenting"), default="")
    mobile_phone = models.CharField(verbose_name=_(
        "Mobile phone"), max_length=17, blank=True, null=True)
    no_of_books_published = models.IntegerField(
        default=0, verbose_name='Number of Books Published')

    class Meta:
        ordering = ['display_name']

    def __str__(self):
        return self.username

# Create Auth Token upon user registration


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
