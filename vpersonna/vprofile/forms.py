from django import forms
from .models import Rule

class RuleForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = ('type_of_service', 'bandwidth_percent','destination_address')
