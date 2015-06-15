from django import forms
from .models import Rule, Client, IPAllocation, News
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.admin import widgets

class RuleForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = ('type_of_service', 'bandwidth_percent','destination_address')

    # add bootstrap design attributes
    def __init__(self, *args, **kwargs):
        super(RuleForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs.update({
                'class': "form-control",
            })

class NewClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'phone_number', 'email', 'card_id', 'address', 'contract_id', 'username', 'password']
        widgets = {'password': forms.PasswordInput()}

    def __init__(self, *args, **kwargs):
        super(NewClientForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs.update({
                'class': "form-control",
            })

class UpdateClientForm(forms.ModelForm):
    password_field = forms.CharField(label='Password', min_length=4, max_length=20, required=False, widget=forms.PasswordInput())
    class Meta:
        model = Client
        fields = ['name', 'phone_number', 'email', 'card_id', 'address', 'contract_id', 'username',]

    def __init__(self, *args, **kwargs):
        super(UpdateClientForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
                'readonly' : True,
        })
        self.fields['contract_id'].widget.attrs.update({
                'readonly' : True,
        })
        for f in self.fields:
            self.fields[f].widget.attrs.update({
                'class': "form-control",
            })

        

class NewAllocationForm(forms.ModelForm):
    class Meta:
        model = IPAllocation
        fields = ['client', 'ip_addr']

    def __init__(self, *args, **kwargs):
        super(NewAllocationForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs.update({
                'class': "form-control",
            })

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'active', 'date'] 
        widgets = {'content': forms.Textarea,
                'date' : forms.DateTimeInput(attrs={'class' : 'date_time_picker form-control'})}
    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)
        for f in self.fields:
            # date field is already set with class attributes, a new widget update will override the old attr values
            if f != 'date':
                self.fields[f].widget.attrs.update({
                    'class': "form-control",
                })
            

class ChangePassword(forms.Form):
    old_password = forms.CharField(label='Old password', max_length=20, min_length=4, widget=forms.PasswordInput())
    new_password = forms.CharField(label='New password', max_length=20, min_length=4, widget=forms.PasswordInput())
    new_confirm_password = forms.CharField(label='Confirm password', max_length=20, min_length=4,widget=forms.PasswordInput())
    
    class Meta:
        fields = ['old_password', 'new_password', 'new_confirm_password'] 

    def __init__(self, *args, **kwargs):
        super(ChangePassword, self).__init__(*args, **kwargs)
        for f in self.fields:
            self.fields[f].widget.attrs.update({
                'class': "form-control",
            })
