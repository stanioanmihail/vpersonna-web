from django import forms
from .models import Rule, Client, IPAllocation, News
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.admin import widgets

class RuleForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = ('type_of_service', 'bandwidth_percent','destination_address')
class NewClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone_number', 'email', 'card_id', 'address', 'contract_id', 'username', 'password']
        widgets = {'password': forms.PasswordInput()}
class UpdateClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone_number', 'email', 'card_id', 'address', 'contract_id', 'username', 'password']
        widgets = {'password': forms.PasswordInput(),}

    def __init__(self, *args, **kwargs):
        super(UpdateClientForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['contract_id'].widget.attrs['readonly'] = True

class NewAllocationForm(forms.ModelForm):
    class Meta:
        model = IPAllocation
        fields = ['client', 'ip_addr']

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'active', 'date'] 
        widgets = {'content': forms.Textarea,
                'date' : forms.DateTimeInput(attrs={'class' : 'date_time_picker'})}
