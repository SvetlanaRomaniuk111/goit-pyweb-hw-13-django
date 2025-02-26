from django import forms
from .models import Author, Quote


class AuthorForm(forms.ModelForm):
    fullname = forms.CharField(max_length=120, required=True,
                               widget=forms.TextInput(
                                   attrs={"class": "form-control"}))
    born_date = forms.CharField(max_length=50, required=False,
                                widget=forms.TextInput(
                                    attrs={"class": "form-control"}))
    born_location = forms.CharField(max_length=120, required=False,
                                    widget=forms.TextInput(
                                        attrs={"class": "form-control"}))
    description = forms.CharField(required=False, widget=forms.Textarea(
        attrs={"class": "form-control"}))

    class Meta:
        model = Author
        fields = ('fullname', 'born_date', 'born_location', 'description')


class QuoteForm(forms.ModelForm):
    quote = forms.CharField(required=True, widget=forms.Textarea(
        attrs={"class": "form-control"}))
    author = forms.ModelChoiceField(queryset=Author.objects.all(),
                                    required=True, widget=forms.Select(
            attrs={"class": "form-control"}))

    class Meta:
        model = Quote
        fields = ('author', 'quote')

    def clean_quote(self):
        quote = self.cleaned_data.get('quote')
        if not quote.startswith('"') or not quote.endswith('"'):
            raise forms.ValidationError('The quote must be enclosed in double quotes (" ").')
        return quote
