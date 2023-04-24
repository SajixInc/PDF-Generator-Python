from django import forms
from .models import User_Profile

#DataFlair #File_Upload
class Profile_Form(forms.ModelForm):

    class Meta:
        model = User_Profile
        fields = [
        'fname',
        
        'display_picture'
        ]