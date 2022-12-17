from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget

# choices = Category.objects.all().values_list('title', 'title')
#
# choice_list = []
# for item in choices:
#     choice_list.append(item)

choice_list = [item for item in Category.objects.all().values_list('title', 'title')]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category','body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of your Post ...'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name of your Title Tag ...'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'user', 'type': 'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add your snippet ...'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Add your post ...'}),
        }

class EditPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag','body', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class AddCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('title', )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
