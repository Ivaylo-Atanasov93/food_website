from django.shortcuts import render


# Create your views here.

def login_view(request):
    context = {}
    return render(request, 'login.html', context)


def sign_up_view(request):
    context = {}
    return render(request, 'sign_up.html', context)
