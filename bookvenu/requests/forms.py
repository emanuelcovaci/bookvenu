from django import forms
from .models import RequestModel


class CreateRequestForm(forms.ModelForm):
    class Meta:
        model = RequestModel
        fields = ['city', 'nrlocuri', 'date',
                  'price', 'phonenumber', 'details',  'finaldate']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreateRequestForm, self).__init__(*args, **kwargs)

    def clean_phonenumber(self):
        phonenumber = self.cleaned_data['phonenumber']
        if phonenumber[0] != '0' or phonenumber[1] != '7' or len(phonenumber) != 10 or phonenumber.isdigit() == False:
            raise forms.ValidationError("Invalid phonenumber")
        return phonenumber

    def clean_price(self):
        price = self.cleaned_data['price']
        if price.isdigit() == False:
            raise forms.ValidationError("Invalid price")
        return price

    def clean_nrlocuri(self):
        nrlocuri = self.cleaned_data['nrlocuri']
        if nrlocuri.isdigit() == False:
            raise forms.ValidationError("Invalid input")
        return nrlocuri


    def clean_city(self):
        city = self.cleaned_data['city']
        return city

    def clean_data(self):
        data = self.cleaned_data['data']
        if data < date.today():
            raise forms.ValidationError("Date is not valid")
        else:
            delta = data - date.today()
            if delta.days > 31:
                raise forms.ValidationError("Task can scheduled with at"
                                            "most 31 days before")
        return data


    def clean_details(self):
        details = self.cleaned_data['details']
        return details

