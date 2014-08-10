from django import forms
from article.models import Article,Comment

class ArticleForm(forms.ModelForm):

    class Meta:
        model=Article
        fields=('title','body','pub_date')

class CommentForm(forms.ModelForm):

    class Meta:
        model=Comment
        fields=('name','body')
