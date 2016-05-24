from django import forms
from django.utils.translation import ugettext_lazy as _
from customers.models import ODCustomer


class ODCustomerForm(forms.ModelForm):
    """
    Form to manage Customer data-entry
    """
    name = forms.CharField(label=_('Nama Customer'))
    email = forms.EmailField(label=_('Email Address'))
    phone = forms.CharField(label=_('Phone Number'))
    address = forms.CharField(label=_('Home Address'))
    picture = forms.ImageField(label=_('Select a profile picture'))

    class Meta:
        model = ODCustomer
        fields = ('name', 'email', 'phone', 'address')