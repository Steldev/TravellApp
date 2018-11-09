from django import forms
from HouseSearch.models import House, HousePhoto, MAX_PRICE, MAX_ROOMS, MAX_SLEEPER


class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['title', 'country', 'city', 'address', 'type',
                  'rooms', 'sleeper', 'price', 'activity', 'about']

        widgets = {
            'title': forms.TextInput(attrs={
                    'class' : 'form-control mb-2',
                    'placeholder' : 'Title',
                }),
            'country': forms.Select(attrs={
                    'class' : 'form-control mb-2'
                }),
            'city': forms.TextInput(attrs={
                    'class' : 'form-control mb-2',
                    'placeholder' : 'City',
                }),
            'address': forms.TextInput(attrs={
                    'class' : 'form-control mb-2',
                    'placeholder' : 'Address',
                }),
            'type': forms.Select(choices=House.HOUSE_TYPE, attrs={
                    'class' : 'form-control mb-2'
                }),
            'rooms': forms.NumberInput(attrs={
                    'class' : 'form-control mb-2',
                    'min' : 1,
                    'max' : MAX_ROOMS,
                }),
            'sleeper': forms.NumberInput(attrs={
                    'class' : 'form-control mb-2',
                    'min' : 1,
                    'max' : MAX_SLEEPER,
                }),

            'price': forms.NumberInput(attrs={
                    'class' : 'form-control mb-2 col-4',
                    'value' : 100,
                    'min' : 1,
                    'max' : MAX_PRICE,
                }),   
            'about': forms.Textarea(attrs={
                    'class' : 'form-control mb-2',
                    'placeholder' : 'About',
                }),
        }

    def save(self, user):
        house = super(HouseForm, self).save(commit=False)
        house.owner = user
        house.save()
        return house

class PhotoForm(forms.ModelForm):
    class Meta:
        model = HousePhoto
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs=
                                     {'name': 'photo',
                                      'multiple': True,
                                      'required': False,
                                      'class' : 'house-edit-images invisible position-absolute',
                                      'accept': 'image/*'
                                      })
        }


class SearchHousesForm(forms.Form):
    country = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'name': 'country',
            'required': False,
            'placeholder': 'Country',
            'title': 'Choice country for search',
            'maxlength': 30,
            'list': 'countries'
        })
    )

    city = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'name': 'city',
            'required': False,
            'placeholder': 'City',
            'title': 'Enter city name for search',
            'maxlength': 40,
        })
    )

    type = forms.MultipleChoiceField(
        required=False,
        choices=House.HOUSE_TYPE,
        widget=forms.CheckboxSelectMultiple(attrs={
            'name': 'type',
            'required': False,
            'checked': True,
            'title': 'Choice house-types for search',
        })
    )
    min_price = forms.DecimalField(
        label='From',
        required=False,
        initial=0.00,
        widget=forms.NumberInput(attrs={
            'name': 'min_price',
            'required': False,
            'title': 'Enter minimum price',
            'min': 0,
            'max': MAX_PRICE,
        })
    )
    max_price = forms.DecimalField(
        label='To',
        required=False,
        initial=MAX_PRICE,
        widget=forms.NumberInput(attrs={
            'name': 'man_price',
            'required': False,
            'title': 'Enter maximum price',
            'min': 0,
            'max': MAX_PRICE,
        })
    )
    rooms = forms.IntegerField(
        required=False,
        initial=1,
        widget=forms.NumberInput(attrs={
            'name': 'rooms',
            'required': False,
            'title': 'Enter rooms count',
            'min': 1,
            'max': MAX_ROOMS,
        })
    )

    sleeper = forms.IntegerField(
        required=False,
        initial=1,
        widget=forms.NumberInput(attrs={
            'name': 'sleeper',
            'required': False,
            'title': 'Enter sleeper count',
            'min': 1,
            'max': MAX_SLEEPER,
        })

    )
    active = forms.BooleanField(
        label='Only active',
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={
            'name': 'active',
            'required': False,
            'title': 'Search only acrive advertisement',
        })
    )
    public = forms.DateField(
        required=False,
        widget=forms.SelectDateWidget(attrs={
            'name': 'public',
            'required': False,
            'title': 'Search advertisement',
        })

    )


    active = forms.BooleanField(
        label='Only active',
        required=False,
        initial=True,
        widget=forms.CheckboxInput(attrs={
            'name': 'active',
            'required': False,
            'title': 'Search only acrive advertisement',
        })
    )
    public = forms.DateField(
        required=False,
        widget=forms.SelectDateWidget(attrs={
            'name': 'public',
            'required': False,
            'title': 'Search advertisement',
        })

    )

    def get_only_full(self):
        """Очистка списка значений полей от пустых полей"""
        dict = self.cleaned_data.copy()

        for key in self.cleaned_data:
            if not (dict[key]) and key != 'type':
                del dict[key]
        return dict
