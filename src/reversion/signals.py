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

    instance.json = instance.serialized_data
