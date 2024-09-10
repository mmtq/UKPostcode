from django import forms

class FeedbackForm(forms.Form):
    text_field = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'px-4 py-3 bg-gray-100 w-full text-sm outline-none rounded',
            'placeholder': 'Enter Postcode Here'
        }),
        required=True,
        label='Enter Postcode Here'
    )

