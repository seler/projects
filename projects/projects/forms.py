from django import forms
from django.utils.translation import ugettext_lazy as _

from mptt.forms import MoveNodeForm

from .models import Component


class ItemForm(forms.Form):
    version = forms.CharField(label=_("version"), max_length=20)
    status = forms.ChoiceField(label=_("status"))
    url = forms.URLField(label=_("url"), required=False)
    file = forms.FileField(label=_("file"), required=False)

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['version'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['file'].widget.attrs['class'] = 'form-control'
        self.fields['url'].widget.attrs['class'] = 'form-control'
        self.fields['url'].widget.attrs['autofocus'] = "autofocus"


class ComponentForm(forms.ModelForm):
    class Meta:
        model = Component
        exclude = ('notepad',)

    def __init__(self, *args, **kwargs):
        project = kwargs.pop('project', None)
        super(ComponentForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = "New component name"
        self.fields['name'].widget.attrs['autofocus'] = "autofocus"

        self.fields['parent'].widget.attrs['class'] = 'form-control'
        self.fields['parent'].widget.attrs['placeholder'] = "None"
        if project:
            self.fields['parent'].queryset = self.fields['parent'].queryset.filter(project=project)


class ComponentDeleteForm(forms.Form):
    component_pk = forms.IntegerField(widget=forms.HiddenInput())


class ComponentNotepadForm(forms.Form):
    notepad = forms.CharField(widget=forms.Textarea())


class ComponentMoveForm(MoveNodeForm):
    pass
