from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from .models import Create
from django.contrib.auth.forms import UserCreationForm
from django import forms
from tinymce.widgets import TinyMCE

class Title(forms.ModelForm):
    class Meta:
        model = Create
        title = forms.CharField(required=False)
        fields = ['title']


class BodyFrom2(forms.Form):
    body = forms.CharField(widget=SummernoteInplaceWidget())


class BodyFrom(forms.ModelForm):
    # body = forms.CharField(widget=SummernoteInplaceWidget())

    def __init__(self, *args, **kwargs):
        super(BodyFrom, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Create
        fields = ['title', 'body', 'rank', 'metadata']
        widgets = {
            'body': TinyMCE(),
        }

# class MainCoinForm(forms.ModelForm):
#     class Meta:
#         model = Create
#         main_coin = Create.metadata_choices
#         main_coin_category = forms.ChoiceField(label=main_coin)
#         fields = ['main_coin_category']
# class Rank(forms.ModelForm):
#     class Meta:
#         model = Create
#         Rank = forms.IntegerField(required=False)
#         fields = ['rank']

# from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
# from django import forms
# from .models import Create
#
#
#
#
# class BodyForm(forms.Form):
#     bar = forms.CharField(widget=SummernoteInplaceWidget())
#
#
# class FormFromSomeModel(forms.ModelForm):
#     class Meta:
#         model = Create
#         widgets = {
#             'bar': SummernoteInplaceWidget(),
#         }
