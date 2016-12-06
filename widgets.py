# -*- mode: python; coding: utf-8; -*-

from django.forms.widgets import Widget
from django.forms.util import flatatt
from django.utils.safestring import mark_safe
from django.core.urlresolvers import reverse
from django import forms

class TagWidgetSelect(forms.SelectMultiple):
    def __init__(self, attrs=None, choices=()):
        super(TagWidgetSelect, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        output = [u'<select%s multiple>' % flatatt(final_attrs)]
        options = self.render_options(value)
        if options:
            output.append(options)
        output.append(u'</select>')
        json_view = reverse('tagging-smartcomplete-json')
        output.append(u"""<script type="text/javascript">
        $(document).ready(function() {
            $("#%s").fcbkcomplete({
              json_url: '%s',
              cache: false,
              filter_case: true,
              filter_hide: true,
                firstselected: true,
              //onremove: "testme",
                //onselect: "testme",
              filter_selected: true,
                maxitems: 5,
              newel: true        
            });		 
        });
        </script>""" % (attrs['id'], json_view))
        return mark_safe(u'\n'.join(output))

    def render_options(self, value):
        if value and type(value) is not list:
            opts = value.split(",")
        else:
            opts = value
        options = ''
        for o in opts:
            options += u'<option value="%s" selected="selected" class="selected">%s</option>' % (o,o)
        return options

    class Media:
        js_base_url = "/tagging_smartcomplete/media"
        css = {
            'all': ('%s/css/tags.css' % js_base_url,)
        }
        js = (
            '%s/js/jquery.min.js' % js_base_url,
            '%s/js/jquery.fcbkcomplete.min.js' % js_base_url,
            )

