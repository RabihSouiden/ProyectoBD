from django.http import HttpResponse
from django.shortcuts import redirect


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapped_func(request, *args, **kwargs):

            group = None
            print(request.user.tipo_usuario)
            if request.user.tipo_usuario:
                group = request.user.tipo_usuario
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else: 
                return HttpResponse('No tienes permiso para entrar')
        return wrapped_func
    return decorator


def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        group = None
        if request.user.tipo_usuario:
            group = request.user.tipo_usuario
        
        if group == 1:
            return redirect('home_propietario')
        if group == 2:
            return redirect('home_veterinaria')
        if group == 3:
            return view_func(request, *args, **kwargs)
    return wrapper_function