# coding=utf-8
from django.apps.config import AppConfig


class ReversionConfig(AppConfig):
    name = "reversion"

    def ready(self):
        super(ReversionConfig, self).ready()
