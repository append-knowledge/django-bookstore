from django import forms
from django.forms import ModelForm
from owner.models import Book,Order

class AddBookForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__"
        widgets={
            'book_name':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.TextInput(attrs={'class':'form-control'}),
            'price':forms.TextInput(attrs={'class':'form-control'}),
            'copies':forms.TextInput(attrs={'class':'form-control'})
        }
    # book_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # author=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # price=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    # copies=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    def clean(self):
        cleaned_data=super().clean()
        book_name=cleaned_data['book_name']
        price=cleaned_data['price']
        copies=cleaned_data['copies']
        books=Book.objects.filter(book_name=book_name)
        if books:
            msg='book with this name already in use'
            self.add_error('book_name',msg)
        if int(price) < 0:
            msg='invalid price'
            self.add_error('price',msg)
        if int(copies)<0:
            msg='invalid input'
            self.add_error('copies',msg)

class EditBook(ModelForm):
    class Meta:
        model=Book
        fields="__all__"
        widgets = {
            'book_name': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'copies': forms.TextInput(attrs={'class': 'form-control'})
        }
    # book_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # author=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # price = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    # copies = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))



class SignUp(forms.Form):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    user_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    conform_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


class SignIn(forms.Form):
    user_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))

class Search_form(forms.Form):
    book_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))


class OrderEditForm(ModelForm):
    # status = forms.CharField(widget=forms.Select(attrs={'class': 'form-control'}))
    # delivery_date = forms.CharField(widget=forms.SelectDateWidget(attrs={'class': 'form-control'}))
    class Meta:
        model=Order
        fields=['status','delivery_date']
        widgets={
            'status':forms.Select(attrs={'class': 'form-control'}),
            'delivery_date':forms.DateInput(attrs={'type':'date'})
        }



