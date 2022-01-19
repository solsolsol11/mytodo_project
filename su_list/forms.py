from django.forms import ModelForm

from su_list.models import SeriousNoUrgentList, SeriousYesUrgentList, NoSeriousNoUrgent, NoSeriousYesUrgent


class SeriousNoUrgentListForm(ModelForm):


    class Meta:
        model = SeriousNoUrgentList
        fields = ['serious_no_urgent']

class SeriousYesUrgentListForm(ModelForm):


    class Meta:
        model = SeriousYesUrgentList
        fields = ['serious_yes_urgent']

class NoSeriousNoUrgentForm(ModelForm):


    class Meta:
        model = NoSeriousNoUrgent
        fields = ['no_serious_no_urgent']

class NoSeriousYesUrgentForm(ModelForm):


    class Meta:
        model = NoSeriousYesUrgent
        fields = ['no_serious_yes_urgent']
