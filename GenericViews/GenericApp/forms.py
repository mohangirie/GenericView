from django import forms


class GenericForms(forms.Form):
    name = forms.CharField(
        label='Name:',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Your Name'
            }
        )
    )
    desc = forms.CharField(
        label='Description:',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Enter Description'
            }
        )
    )
