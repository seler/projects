from django import forms
from django.utils.translation import ugettext_lazy as _
from .models import Component


class ItemForm(forms.Form):
    version = forms.CharField(label=_("version"), max_length=20)
    status = forms.ChoiceField(label=_("status"))
    url = forms.URLField(label=_("url"), required=False)
    file = forms.FileField(label=_("file"), required=False)


class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component

    def __init__(self, *args, **kwargs):
        super(ComponentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = "New component name"
