from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from .forms import CreateUserForm, ProfileInformationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from manjorno_v3.decorators import unauthenticated_user, allowed_users
# Create your views here.
from .models import Customer, ProfileInformation


@allowed_users(allowed_roles=['customer', 'delivery', 'admin'])
def user_detail_view(request):
    customer = request.user.customer.user.customer
    profile_info = customer.profileinformation
    context = {'profile_info': profile_info}
    return render(request, 'profile_details.html', context)


@allowed_users(allowed_roles=['customer', 'delivery', 'admin'])
def user_profile_view(request):
    context = {}
    customer = request.user.customer.user.customer
    profile_info, create = ProfileInformation.objects.update_or_create(customer=customer)
    # if profile_info.completed:
    #     return redirect('profile_details')
    form = ProfileInformationForm(request.POST or None, instance=profile_info)
    if form.is_valid():
        form.save()
        profile_info.email = customer.email
        profile_info.completed = True
        profile_info.save()
        return redirect('profile_details')
    context['form'] = form
    return render(request, 'create_user_profile.html', context)


@unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile_update')
        else:
            messages.info(request, 'Username OR Password is incorrect')
    context = {}
    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


@unauthenticated_user
def sign_up_view(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data['username']

            email = form.cleaned_data['email']
            Customer.objects.create(user=user, email=email)
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request, f'Account was created for {form.cleaned_data.get("username")}')
            return redirect('login')
    context = {'form': form}
    return render(request, 'sign_up.html', context)
