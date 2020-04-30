from django import forms
from ckeditor.widgets import CKEditorWidget


class CommentForm(forms.Form):
    course_id = forms.IntegerField(widget=forms.HiddenInput)
    chapter_num = forms.IntegerField(widget=forms.HiddenInput)
    text = forms.CharField(widget=CKEditorWidget())

    def clean(self):
        course_id = self.cleaned_data['course_id']
        chapter_num = self.cleaned_data['chapter_num']
        text = self.cleaned_data['text']
        if chapter_num and course_id and text:
            return self.cleaned_data
        else:
            raise forms.ValidationError('评论对象不存在')
