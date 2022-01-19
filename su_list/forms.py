from django.forms import ModelForm

from su_list.models import Sulist


class SulistForm(ModelForm):


    class Meta:
        model = Sulist
        fields = ['serious_no_urgent']
