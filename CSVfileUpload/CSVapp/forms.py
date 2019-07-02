from django import forms
from CSVapp.models import form

class EventsForm(forms.ModelForm):
    class Meta:
        model = form
        fields = "__all__"