from django import forms

class create_new_list(forms.Form):
    name = forms.CharField(label="Name", max_length=200)