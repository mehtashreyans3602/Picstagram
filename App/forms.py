from dataclasses import fields
from django.forms import ModelForm
from .models import EditProfile, Post
from django.contrib.auth.models import User

class profileForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','username', 'email']
        help_texts = {
            'username':None
        }
class EditProfileForm(ModelForm):
    class Meta:
        model = EditProfile
        fields = ('image', 'bio', 'phoneNo', 'gender')

class AddPostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['image' , 'caption']
        
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(AddPostForm, self).save(commit=False)
        instance.author = self.request.user
        if commit: 
            instance.save()
        return instance
