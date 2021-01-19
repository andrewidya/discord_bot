from django.forms import ModelForm, widgets
from suit.widgets import AutosizedTextarea


class AdditionalPropertiesForm(ModelForm):
    class Meta:
        widgets = {
            'description': AutosizedTextarea(attrs={'row': 1, 'class': 'input-xlarge'})
        }