from django.shortcuts import redirect

def sign_in_required(func):

    def wrapper(request,id=None,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect('signin')
        else:
            return fucn(request,id=None,*args,**kwargs)
    return wrapper