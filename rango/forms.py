# coding: UTF-8

from django import forms
from django.conf import settings
from django.contrib.auth.models import User
from rango.models import Category, CatPage, SubPage, BaiduEditor, UserOOXX

# from captcha.fields import ReCaptchaField


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")
    no = forms.CharField(max_length=20, help_text="Please enter the course code.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    url = forms.URLField(max_length=200, help_text="Please enter the index URL of the course.")

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name', 'no', 'url')


class CatPageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200,
                         help_text="Please enter the URL of the page.",
                         initial="http://")

    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = CatPage

        fields = ('title', 'url')

    def clean(self):
        # print "cleaning"
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data


class SubPageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = SubPage

        fields = ('title', 'url', )

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', )


# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('gender', 'facebook', 'wechat', )


class TestUeditorModelForm(forms.ModelForm):

    class Meta:
        model = BaiduEditor
        fields = ('content',)


# class FormWithCaptcha(forms.Form):
#     captcha = ReCaptchaField(
#         public_key=settings.RECAPTCHA_PUBLIC_KEY,
#         private_key=settings.RECAPTCHA_PRIVATE_KEY,
#         use_ssl=True
#     )


class UserOOXXForm(forms.ModelForm):

    class Meta:
        model = UserOOXX
        fields = ('name', 'attr', )


