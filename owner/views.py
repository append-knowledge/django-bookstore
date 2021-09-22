from django.shortcuts import render, redirect

from owner import forms
# Create your views here.
from owner.models import Book,Order
from django.db.models import Count



def home(request):
    return render(request, "index.html")


# 8000/owner/book/add

def books_add(request):
    form = forms.AddBookForm()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = forms.AddBookForm(request.POST,request.FILES)
        if form.is_valid():
            # book_name = form.cleaned_data['book_name']
            # author = form.cleaned_data['author']
            # price = form.cleaned_data['price']
            # copies = form.cleaned_data['copies']
            # book=Book(book_name=book_name,author=author,price=price,copies=copies)
            # book.save()
            form.save()


            return redirect('booklist')
        else:
            return render(request, 'book_add.html', {'form': form})
    return render(request, 'book_add.html', context)


def books_edit(request,id):
    book=Book.objects.get(id=id)
    # data={
    #     'book_name':book.book_name,
    #     'author':book.author,
    #     'price':book.price,
    #     'copies':book.copies
    # }
    form = forms.EditBook(instance=book)
    context = {}
    context['form'] = form
    if request.method=='POST':
        form=forms.EditBook(request.POST,instance=book,file=request.FILES)
        if form.is_valid():
            # b_name = form.cleaned_data['book_name']
            # author = form.cleaned_data['author']
            # price = form.cleaned_data['price']
            # copies = form.cleaned_data['copies']
            # book.book_name=b_name
            # book.author=author
            # book.price=price
            # book.copies=copies
            # book.save()
            form.save()

            return redirect('booklist')



    return render(request, 'book_edit.html', context)


def books_delete(request,id):
    book=Book.objects.get(id=id)
    book.delete()
    return redirect('booklist')



def signup(request):
    form = forms.SignUp
    context = {'form': form}
    if request.method == "POST":
        form = forms.SignUp(request.POST)
        if form.is_valid():
            return redirect("signin")
    return render(request, 'sign_up.html', context)


def signin(request):
    form = forms.SignIn
    context = {'form': form}
    if request.method == "POST":
        form = forms.SignIn(request.POST)
        if form.is_valid():
            return redirect("books/home")
    return render(request, 'sign_in.html', context)


def book_list(request):
    form=forms.Search_form()

    books = Book.objects.all()
    context={}
    context['books']=books

    context['form']=form
    if request.method=='POST':
        form=forms.Search_form(request.POST)
        if form.is_valid():
            book_name=form.cleaned_data['book_name']
            books=Book.objects.filter(book_name__contains=book_name)
            context['books']=books
            return render(request,'book_list.html',context)
    return render(request, 'book_list.html', context)

def book_detail(request,id):
    book=Book.objects.get(id=id)
    context={}
    context['book']=book
    return render(request,'book_detail.html',context)


def owner_dashboard(request):
    reports=Order.objects.values("products__book_name").annotate(counts=Count('products')).exclude(status='cancel')
    books=Book.objects.all().order_by('copies')

    orders=Order.objects.filter(status='ordered')
    context={'orders':orders,"reports":reports,'books':books}
    return render(request,'dashboard.html',context)

def owner_edit(request,id):
    form=forms.OrderEditForm()
    order=Order.objects.get(id=id)
    context={'form':form}
    if request.method=='POST':
        form=forms.OrderEditForm(request.POST,instance=order)
        if form.is_valid():
            book=Book.objects.get(id=order.products.id)
            if order.status=='cancel':
                book.copies+=1
                book.save()
            form.save()
            return redirect('dashboard')

    return render(request,'dashedit.html',context)

