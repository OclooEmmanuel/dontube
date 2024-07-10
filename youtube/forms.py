from django import forms


class Youtube(forms.Form):
    urlbox = forms.URLField(
        max_length='100', widget=forms.TextInput(attrs={
            'class' : 'form-control p-4 border-3 rounded-4', 
            'placeholder':'past link here'
            
            }))
    
    # urlbox = forms.CharField(
    #     max_length=100,
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Enter your name'
    #     }))