from django import forms
from .models import Shortener

class ShortenerForm(forms.ModelForm):
    origin_url = forms.URLField(widget=forms.URLInput(
        attrs={"class": "w-full md:w-70% px-5 mb-5 md:mb-0 rounded-md h-16 my-box focus:bg-white focus:outline-none active:outline-8 transition-all duration-300 ease-in-out", "placeholder": "Your URL to shorten"}))
    class Meta:
        model = Shortener
        fields = ('origin_url',)