# -*- mode: python; coding: utf-8; -*-

from django import forms
from django.utils.translation import ugettext_lazy as _

from tagging_smartcomplete import settings

class TagFieldSelect(forms.MultipleChoiceField):
    """
    A ``CharField`` which validates that its input is a valid list of
    tag names.
    """

    def __init__(self, max_length=None, min_length=None, *args, **kwargs):
        super(TagFieldSelect, self).__init__(*args, **kwargs)


    def clean(self, value):
        if not value:
            return ''
        for tag_name in value:
            if len(tag_name) < settings.MIN_TAG_LENGTH:
                raise forms.ValidationError(
                    _('Each tag may be no less than %s characters long.') %
                        settings.MIN_TAG_LENGTH)
            if len(tag_name) > settings.MAX_TAG_LENGTH:
                raise forms.ValidationError(
                    _('Each tag may be no more than %s characters long.') %
                        settings.MAX_TAG_LENGTH)
        return ','.join(value)
