from django.shortcuts import render,redirect
from customer import forms
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from owner.models import Book,Order
from customer.filters import BookFilter
from customer.decorators import sign_in_required




# Create your views here.
def sign_up(request):
    form=forms.SignUpregistration()
    context={}
    context['form']=form
    if request.method=='POST':
        form=forms.SignUpregistration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')


    return render(request,'customer/sign_up.html',context)

def sign_in(request):
    form=forms.SignInRegistration()
    context={}
    context['form']=form
    if request.method=='POST':
        form=forms.SignInRegistration(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)
                return redirect('home')
            else:
                messages.error(request, 'invalid credentials')
                return redirect('signin')
        else:
            return render(request,'customer/sign_in.html',{'form':form})

    return render(request,'customer/sign_in.html',context)

@sign_in_required
def sign_out(request,*args,**kwargs):

    logout(request)
    return redirect('signin')

@sign_in_required
def base_home(request,*args,**kwargs):

    books=Book.objects.all()
    context={'books':books}
    print(books)
    return render(request,'customer/user_home.html',context)

@sign_in_required
def order_create(request,p_id,*args,**kwargs):

    book=Book.objects.get(id=p_id)
    form=forms.Order_form(initial={'products':book})
    context={'form':form,'book':book}

    if request.method=='POST':
        form=forms.Order_form(request.POST)
        if form.is_valid():
            order=form.save(commit=False)
            order.user=request.user
            book.copies-=1
            book.save()
            order.save()
            messages.success(request,'successfully ordered book')
            return redirect('home')

    return render(request,'customer/order_create.html',context)

@sign_in_required
def my_orders(request,*args,**kwargs):

    orders=Order.objects.filter(user=request.user).exclude(status='cancel')
    context={'orders':orders}
    return render(request,'customer/my_orders.html',context)

@sign_in_required
def order_remove(request,id,*args,**kwargs):

    order=Order.objects.get(id=id)
    order.status='cancel'
    book=Book.objects.get(id=order.products.id)
    book.copies+=1
    book.save()
    order.save()
    return redirect('my_orders')

@sign_in_required
def book_find(request,*args,**kwargs):
    filter=BookFilter(request.GET,queryset=Book.objects.all())

    return render(request,'customer/book_filter.html',{'filter':filter})
