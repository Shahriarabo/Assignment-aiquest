from django.core import validators
from django import forms

class Registesion(forms.Form):
    frist_name = forms.CharField(min_length=5, max_length=15)
    last_name = forms.CharField(min_length=5, max_length=15)
    email = forms.EmailField(max_length=25)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=15)
    comfrom_password = forms.CharField(widget=forms.PasswordInput, min_length=8, max_length=15)
    which_one_flowers = forms.IntegerField(min_value=3, max_value=20)
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':4,'cols':20}))
    Agree_to_terms_and_conditions = forms.CharField(widget=forms.CheckboxInput)
    Do_you_want_to_buy_flowers_in_my_shop = forms.BooleanField()
    
    
    

    def emails(self):
        email_matchs = super().emails()
        email_match = self.cleaned_data['email']
        re_email_match = self.cleaned_data['comfrom_email']
        if email_match != re_email_match:
            raise forms.ValidationError("Email doesn't match")
        
        
        
        
    def clean(self):
        cleaned_data = super().clean()
        password_match = self.cleaned_data['password']
        re_password_match = self.cleaned_data['comfrom_password']
        if password_match != re_password_match:
            raise forms.ValidationError("Password doesn't match")
        
    
    
    
