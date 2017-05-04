from django import forms
from datetime import date
from .models import EventModel,Comment,Reserve
from category.models import Category
from django.shortcuts import get_object_or_404


class CreateEventForm(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = ['name', 'adress', 'nrlocuri', 'date',
                  'price', 'phonenumber', 'details', 'category',
                  'image1', 'image2', 'image3', 'image4', 'site', 'finaldate']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(CreateEventForm, self).__init__(*args, **kwargs)

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
        if name.isdigit():
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

    def clean_site(self):
        site = self.cleaned_data['site']
        return site

    def clean_category(self):
        category = get_object_or_404(Category,
                                     name=self.cleaned_data['category'])
        return category

    def clean_image4(self):
        image1 = self.cleaned_data['image1']
        image2 = self.cleaned_data['image2']
        image3 = self.cleaned_data['image3']
        image4 = self.cleaned_data['image4']
        image_names = []
        if (image1 and not isinstance(image1, (int, float))):
            image_names.append(image1.name)
        if (image2 and not isinstance(image2, (int, float))):
            image_names.append(image2.name)
        if (image3 and not isinstance(image3, (int, float))):
            image_names.append(image3.name)
        if (image4 and not isinstance(image4, (int, float))):
            image_names.append(image4.name)
        if (len(image_names) - 1 == len(set(image_names))):
            raise forms.ValidationError("You can't upload 2 images"
                                        "that are the same")
        return image4

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['body']



class Edit_Post(forms.ModelForm):
    class Meta:
        model = EventModel
        fields = ['name', 'adress', 'nrlocuri', 'date',
                  'price', 'phonenumber', 'details']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(Edit_Post, self).__init__(*args, **kwargs)

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
        if name.isdigit():
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



class ReserveForm(forms.ModelForm):
    class Meta:
        model = Reserve
        fields = ['nrlocuri']

    def clean_nrlocuri(self):
        nrlocuri = self.cleaned_data['nrlocuri']
        if nrlocuri.isdigit() == False:
            raise forms.ValidationError("Invalid input")
        if int(nrlocuri) < 1 or int(nrlocuri)> 20:
            raise forms.ValidationError("Not enough/Too many tickets")
        return nrlocuri