from django import forms
from django.contrib.auth.models import User
from rango.models import Page, Category, UserProfile

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the auction.")
    description = forms.CharField(max_length=1000,
                            help_text="Please enter the description of the auction.")
    startprice = forms.FloatField(help_text="Please enter the startprice of the auction.")
    closingtime = forms.DateTimeField(help_text="Please enter the closetime of the auction.")
    picture = forms.ImageField(required=False)
    url = forms.URLField(max_length=200,
                         help_text="Please enter the URL of the auction.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    number = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    status = forms.CharField(widget=forms.HiddenInput(), initial='open')
    highestprice = forms.FloatField(widget=forms.HiddenInput(), initial=startprice)
    bestbidder = forms.CharField(widget=forms.HiddenInput(), initial='')
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Page

        # What fields do we want to include in our forms?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them.
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category','owner',)
        # or specify the fields to include (i.e. not include the category field)
        # fields = ('title', 'url', 'views')

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://',
        # then prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    name = forms.CharField(required=False)
    email = forms.URLField(required=False)
    phone = forms.CharField(required=False)
    address = forms.CharField(required=False)
    picture = forms.ImageField(required=False)
    description = forms.CharField(required=False)

    class Meta:
        model = UserProfile
        exclude = ('user', 'bidlist', 'ownlist')