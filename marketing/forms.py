from django import  forms
from marketing.models import *


class SettingForm(forms.ModelForm):
    class Meta:
        model = Setting
        fields = "__all__"

    # IN the ifitial giving the forms the class name for bootstrap
    def __init__(self , *args , **kwargs):
        super(SettingForm , self).__init__(*args , **kwargs)
        self.fields['token'].widget.attrs.update({'class':'form-control'})
        self.fields['phone'].widget.attrs.update({'class':'form-control'})
        self.fields['logger'].widget.attrs.update({'class':'form-control'})
        self.fields['update_check'].widget.attrs.update({'class':'form-control'})