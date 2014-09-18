from django import forms
from django.utils.translation import ugettext_lazy as _


class ItemForm(forms.Form):
    version = forms.CharField(label=_("version"), max_length=20)
    status = forms.ChoiceField(label=_("status"))
    url = forms.URLField(label=_("url"), required=False)
    file = forms.FileField(label=_("file"), required=False)
