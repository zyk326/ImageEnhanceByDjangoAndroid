from django import forms
from .models import Font

class FormFromT(forms.Form):
    title = forms.CharField(max_length=20, min_length=2, label="标题",
                            error_messages={
                                "min_length" : 'min_length error 2',
                                "max_length" : 'max_length error 20',
                            })
    content = forms.CharField(widget=forms.Textarea, label='内容')
    email = forms.EmailField(label='邮箱')

class FormFromM(forms.ModelForm):
    class Meta:
        model = Font
        fields = "__all__"