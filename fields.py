# -*- mode: python; coding: utf-8; -*-

from django.contrib.admin.widgets import AdminTextInputWidget
from tagging import settings

from tagging.fields import TagField
from tagging_smartcomplete.forms import TagFieldSelect
from tagging_smartcomplete.widgets import TagWidgetSelect


class TagFieldSmartcomplete(TagField):


    def formfield(self, **kwargs):
        defaults = {'form_class': TagFieldSelect}
        defaults['widget'] = TagWidgetSelect
        defaults.update(kwargs)

        # As an ugly hack, we override the admin widget
        if defaults['widget'] == AdminTextInputWidget:
            defaults['widget'] = TagWidgetSelect
        return super(TagFieldSmartcomplete, self).formfield(**defaults)
