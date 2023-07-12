from django import forms
from django.forms import NumberInput

class MemberForm(forms.Form):
    
    mid = forms.IntegerField(required=False,widget=forms.NumberInput(attrs={'style': 'width: 300px;'}))
    mname = forms.CharField()
    memail = forms.EmailField()
    mnumber = forms.IntegerField()
    