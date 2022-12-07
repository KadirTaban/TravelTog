from django import forms
from django import forms
from .models import PostModel, Comment

class PostModelForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ['title', 'content','image','image_2','image_3']

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title','content')

class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label = '',widget=forms.TextInput(attrs={'placeholder':'Add'})
    )
    class Meta:
        model = Comment
        fields = ('content',)