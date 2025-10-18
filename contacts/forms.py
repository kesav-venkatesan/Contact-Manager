from django import forms
from .models import Contact
from django.core.exceptions import ValidationError

from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'input input-bordered w-full',
            'placeholder': 'Contact Name'
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'input input-bordered w-full',
            'placeholder': 'Contact Email'
        })
    )

    file = forms.FileField(
        widget=forms.FileInput(attrs={
            'class': 'file-input file-input-bordered w-full',
            
        }),
        required=False
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        if Contact.objects.filter(user=self.initial.get('user'),email=email).exists():
            raise ValidationError("You alread have the Contact with this email")
        return email

    class Meta:
        model = Contact
        fields = ('name', 'email','file')