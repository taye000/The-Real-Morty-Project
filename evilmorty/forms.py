from django import forms

class fileform(forms.forms):
    title = forms.CharField(max_length=50)
    file = forms.FileField()