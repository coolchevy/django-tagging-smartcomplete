# -*- mode: python; coding: utf-8; -*-

from django.conf import settings

# The maximum and minimum length of a tag's name.
MAX_TAG_LENGTH = getattr(settings, 'MAX_TAG_LENGTH', 50)
MIN_TAG_LENGTH = getattr(settings, 'MIN_TAG_LENGTH', 3)
