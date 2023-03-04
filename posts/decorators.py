from django.shortcuts import redirect
from django.contrib import messages

def unAuthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('frontend')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func