from django import forms
from .models import EventModel

class EventForm(forms.Form):

    class Meta:
        model = EventModel
        fields = ['name', 'adress', 'nrlocuri', 'date', 'price', 'phonenumber', 'details', 'category']
        widgets = {
            'name': forms.TextInput({'required': 'required', 'placeholder': 'Name'}),
            'adress': forms.TextInput({'required': 'required', 'placeholder': 'Adress'}),
            'nrlocuri': forms.TextInput({'required': 'required', 'placeholder': 'Nr.Locuri'}),
            'date': forms.TextInput({'required': 'required', 'placeholder': 'Date'}),
            'price': forms.TextInput({'required': 'required', 'placeholder': 'Price'}),
            'phonenumber': forms.TextInput({'required': 'required', 'placeholder': 'Phone Number'}),
            'details': forms.TextInput({'required': 'required', 'placeholder': 'Details'}),
            'category': forms.TextInput({'required': 'required', 'placeholder': 'Category'}),
        }
    def clean_phonenumber(self):
        phonenumber = self.cleaned_data['phonenumber']
        if phonenumber[0] != '0' or phonenumber[1] != '7' or len(phonenumber) != 10 or phonenumber.isdigit() == False:
            raise forms.ValidationError("Invalid phonenumber")
        return phonenumber
    def clean_price(self):
        price = self.cleaned_data['price']
        if phonenumber.isdigit() == False:
            raise forms.ValidationError("Invalid price")
        return price

    def clean_nrlocuri(self):
        nrlocuri = self.cleaned_data['nrlocuri']
        if nrlocuri.isdigit() == False:
            raise forms.ValidationError("Invalid input")
        return nrlocuri