from django import forms
from .models import *

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'imgfile', 'category']
        labels = {
            'title': '제목',
            'content': '내용',
            'imgfile': '이미지 삽입',
            'category': '태그'
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']


class RecommentForm(forms.ModelForm):

    class Meta:
        model = Recomment
        fields = ['content', 'comment']