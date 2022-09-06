from django import forms

class userForms(forms.Form):
    num1 = forms.CharField(label='value1', required=False)
    num2 = forms.CharField(label='value2')