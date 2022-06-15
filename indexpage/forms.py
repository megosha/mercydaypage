from django import forms

class Registartion(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Имя Фамилия',
                                                                        'data-error':'Введите ваше имя',
                                                                        'oninput': 'valid_name(this.id)'}))
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Телефон',
                                                                        'data-error':'Введите номер вашего телефона',
                                                                         'oninput': 'valid_phone(this.id)'}))