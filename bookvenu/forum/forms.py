from django import forms
from .models import Thread,ThreadComment

class ThreadForm(forms.ModelForm):

    class Meta:
        model = Thread
        fields = ['name','body']

    def init(self, args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(ThreadForm, self).init(args, **kwargs)

class ThreadCommentForm(forms.ModelForm):

    class Meta:
        model = ThreadComment
        fields = ['body']