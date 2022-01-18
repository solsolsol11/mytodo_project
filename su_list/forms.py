from django.forms import ModelForm

from su_list.models import Sulist


class SulistForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['serious_no_urgent'].required = True
        self.fields['serious_yes_urgent'].required = True
        self.fields['no_serious_no_urgent'].required = True
        self.fields['no_serious_yes_urgent'].required = True

    class Meta:
        model = Sulist
        fields = ['serious_no_urgent', 'serious_yes_urgent', 'no_serious_no_urgent', 'no_serious_yes_urgent']
