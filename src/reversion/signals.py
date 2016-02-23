import json
from django.db.models.signals import pre_save
from django.dispatch.dispatcher import Signal, receiver

# Version management signals.
from reversion.models import Version

pre_revision_commit = Signal(providing_args=["instances", "revision", "versions"])
post_revision_commit = Signal(providing_args=["instances", "revision", "versions"])


@receiver(pre_save, sender=Version)
def store_json(sender, **kwargs):
    instance = kwargs.get('instance', None)

    if not instance:
        return

    if instance.format != 'json':
        raise NotImplementedError(
            "%s format is not implemented yet" % instance.format
        )

    # django default encoder encodes object via list:
    # [{ ... fields }] instead of { ...fields } for security reasons
    # so we need to make this stupid transformation
    # bad.. very bad, but there is no ideas at the time to do it another way
    # quickly
    # so it is todo! find more elegant way for it
    try:
        instance.json = json.loads(instance.serialized_data)[0]
    except IndexError:
        instance.json = {}
