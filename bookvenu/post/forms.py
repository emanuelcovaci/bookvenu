from django import forms
from datetime import date
from .models import EventModel

class EventForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = ['name', 'adress', 'nrlocuri', 'date', 'price', 'phonenumber', 'details', 'category','image1','image2','image3','image4']
        widgets = {
            'name': forms.TextInput({'required': 'required', 'placeholder': 'Name'}),
            'adress': forms.TextInput({'required': 'required', 'placeholder': 'Adress'}),
            'nrlocuri': forms.TextInput({'required': 'required', 'placeholder': 'Nr.Locuri'}),
            'date': forms.TextInput({'required': 'required', 'placeholder': 'Date format YYYY-MM-DD'}),
            'price': forms.TextInput({'required': 'required', 'placeholder': 'Price'}),
            'phonenumber': forms.TextInput({'required': 'required', 'placeholder': 'Phone Number'}),
            'details': forms.TextInput({'required': 'required', 'placeholder': 'Details'}),
            'category': forms.TextInput({'required': 'required', 'placeholder': 'Category'}),
            'image1': forms.ImageField({'required': 'required'}),
            'image2': forms.ImageField({'required': 'required'}),
            'image3': forms.ImageField({'required': 'required'}),
            'image4': forms.ImageField({'required': 'required'}),
        }

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

    def clean_name(self):
        name = self.cleaned_data['name']
        if (
                not (name.isalnum())
        ):
            raise forms.ValidationError("Name contains invalid characters")
        return name

    def clean_adress(self):
        adress = self.cleaned_data['adress']
        return adress

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

    def clean_category(self):
        category = self.cleaned_data['category']
        return category

    def clean_image4(self):
        image = self.cleaned_data['image1']
        image2 = self.cleaned_data['image2']
        image3 = self.cleaned_data['image3']
        image4 = self.cleaned_data['image4']
        image_names = []
        if(image1 and not isinstance(image1, (int, float))):
            image_names.append(image1.name)
        if(image2 and not isinstance(image2, (int, float))):
            image_names.append(image2.name)
        if(image3 and not isinstance(image3, (int, float))):
            image_names.append(image3.name)
        if(image4 and not isinstance(image4, (int, float))):
            image_names.append(image4.name)
        if(len(image_names)-1 == len(set(image_names))):
            raise forms.ValidationError("You can't upload 2 images"
                                        "that are the same")
        return image4