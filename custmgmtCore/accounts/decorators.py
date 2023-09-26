from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func

def allowed_users(allowed_roles=[]):
    def decorators(view_func):
        def wrapper_func(request,*args,**kwargs):

            groups=None
            if request.users.groups.exists():
                group = request.users.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request,*args,**kwargs)
            else:
                return HttpResponse('you are not allowed to view this page')
        return wrapper_func
    return decorators
def admin_only(view_func):
    def wrapper_function(request,*args,**kwargs):
        group=None
        if request.users.groups.exists():
            group = request.users.groups.all()[0].name
        if group =='customer':
            return redirect('user-page')
        if group =='admin':
            return view_func(request,*args,**kwargs)
    return wrapper_function
