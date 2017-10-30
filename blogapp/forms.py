from django.contrib.auth.models import User
from django import forms
from .models import blog

class AddBlogForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea)
    content = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = blog
        fields = ['name','title', 'description','blog_image','content']
