from .models import *
from django.forms import ModelForm, EmailInput, IntegerField, TextInput, PasswordInput


class PostCommentForm(ModelForm):
    class Meta:
        model = PostComment
        fields = '__all__'

        widgets = {
            'email': EmailInput(attrs={
                'class':'field_custom',
                'placeholder':'Email'}),
            'phone': TextInput(attrs={
                'class': 'field_custom',
                'placeholder': 'Phone'}),
            'password': PasswordInput(attrs={
                'class': 'field_custom',
                'placeholder': 'Password'}),
            'comment': TextInput(attrs={
                'class': 'field_custom',
                'placeholder': 'Comment'})
        }