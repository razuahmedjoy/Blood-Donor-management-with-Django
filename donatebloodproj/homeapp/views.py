from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from .forms import DonorRegistrationForm, DonorUpdateform

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


from django.contrib import messages
from .models import Donor
from django.contrib.auth.models import User

from .filters import DonorFilter
# Create your views here.


def home(request):
    donors = Donor.objects.filter(status='active').order_by('-id')

    donorfilter = DonorFilter(request.GET, queryset=donors)
    donors = donorfilter.qs

    context = {'donors': donors,
               'donorfilter': donorfilter, }

    return render(request, 'home.html', context)


def alldonors(request):

    donors = Donor.objects.filter(status='active')

    donorfilter = DonorFilter(request.GET, queryset=donors)
    donors = donorfilter.qs

    context = {'donors': donors,
               'donorfilter': donorfilter, }

    return render(request, 'all-donors.html', context)


@login_required
def profile(request):
    donor = Donor.objects.get(user=request.user)
    if donor:
        context = {
            'donor': donor,
        }
        return render(request, 'profile.html', context)
    else:
        return redirect('donorupdate')


def register(request):
    if request.user.is_authenticated:
        return redirect('donorupdate')

    form = DonorRegistrationForm()
    if request.method == 'POST':
        form = DonorRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            donordata = Donor()
            donordata.user = user
            donordata.contact_no = user.username
            donordata.save()
            if user is not None:

                print("authenticated")
                login(request, user)

                print("logged in")

                return redirect('donorupdate')

            return redirect('home')

    context = {
        'title': 'রক্তদাতা হিসেবে রেজিস্ট্রেশন করুন',
        'form': form,
    }
    return render(request, 'register.html', context)


@login_required
def update_profile(request):
    current_user = Donor.objects.get(user=request.user)
    form = DonorUpdateform(instance=current_user)
    if request.method == "POST":
        form = DonorUpdateform(request.POST, instance=current_user)
        if form.is_valid():
            newcontact = form.cleaned_data.get("contact_no")

            if newcontact != request.user.username:
                user = User.objects.filter(username=newcontact)
                if user:
                    messages.warning(
                        request, "এই নাম্বার দিয়ে আরেকটি একাউন্ট রয়েছে । একটি নাম্বার দিয়ে কেবল একটি একাউন্টই খোলা যাবে")
                    return redirect('donorupdate')
                else:
                    updateuser = User.objects.get(
                        username=request.user.username)
                    updateuser.username = newcontact
                    updateuser.save()

            form.save()

            donordata = Donor.objects.get(user=request.user)

            if donordata.status == 'deactivate':
                donordata.status = 'active'
                donordata.save()
                form = DonorUpdateform(instance=current_user)
                return redirect('donorupdate')

    context = {
        'title': "আপনার তথ্য আপডেট করুন",
        'form': form,
        'current_donor': current_user,
    }
    return render(request, 'donorupdate.html', context)


def loginview(request):
    if request.user.is_authenticated:
        return redirect('donorupdate')
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get(
            'username'), password=request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('donorupdate')
        else:
            messages.warning(
                request, "আপনার কন্টাক্ট নাম্বার বা পাসওয়ার্ড ভুল হয়েছে")
    context = {
        'title': 'লগিন করুন'
    }
    return render(request, 'login.html', context)


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))
