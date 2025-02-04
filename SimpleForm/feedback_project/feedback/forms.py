from django import forms

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length=100, label="Your Name: ")
    email = forms.EmailField(label="Your Email: ")
    message = forms.CharField(label="Your Message:", widget=forms.Textarea)
    