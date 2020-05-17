from django.contrib.auth.models import User
from django.db.models.signals import post_save


from profile_page.models import Profile


def create_profile(sender, instance, created, **kwargs):
    if created:
        values = {}
        for field in sender._meta.local_fields:
            values[field.attname] = getattr(instance, field.attname)
        user = Profile(**values)
        user.save()


post_save.connect(create_profile, User)
