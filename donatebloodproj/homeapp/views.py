from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse
from .forms import DonorRegistrationForm, DonorUpdateform

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import *
from django.contrib.auth.models import User

import requests
import json
import random
import re
from django.http import HttpResponse,JsonResponse

from .filters import DonorFilter
# Create your views here.




def home(request):
    donors = Donor.objects.filter(status='active').order_by('-id')

    donorfilter = DonorFilter(request.GET, queryset=donors)
    donors = donorfilter.qs

    context = {'donors': donors,
               'donorfilter': donorfilter, }

    return render(request, 'home.html', context)



def shurur_kotha(request):
    shurur_kotha = suruKotha.objects.last()
    return render(request,"shururkotha.html",context={"shurur_kotha":shurur_kotha})


def volunteers(request):
    volunteers = Volunteer.objects.filter(is_active = True)
    context = {
        'volunteers':volunteers,
        'title' : "ভলান্টিয়ার্স",
    }
    return render(request,"volunteers.html",context)

def mentors(request):
    volunteers = Mentor.objects.filter(is_active = True)
    context = {
        'volunteers':volunteers,
        'title' : "মেন্টর",
    }
    return render(request,"volunteers.html",context)

def advisers(request):
    volunteers = Adviser.objects.filter(is_active = True)
    context = {
        'volunteers':volunteers,
        'title' : "উপদেষ্টা",
    }
    return render(request,"volunteers.html",context)


def shohojogiview(request):
    shohojogiOrg = shohojogi.objects.all()

    context = {
        "shohojogiOrg" : shohojogiOrg,
        "title": "সহযোগী প্রতিষ্ঠান", 
    }

    return render(request,"shohojogi.html",context)

def blog_home(request):
    blogs = Blog.objects.all()
    context = {
        "blogs":blogs,
        "title": "Blogs"
    }
    return render(request,"blogs.html",context)


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



def send_sms(contact_no,message):
    
    url = f"http://fsms.fantasyhost.com.bd:6005/api/v2/SendSMS?ApiKey={settings.APIKEY}&ClientId={settings.CLIENTID}&SenderId={settings.SENDERID}&Message={message}&MobileNumbers={contact_no}&Is_Unicode=true"

    payload  = {}
    headers = {
    'Content-Type': 'application/json'
    }
    try:
        response = requests.request("GET", url, headers=headers, data = payload)
    except:
        response = None
    
    return response


def register(request):
    otpsent = False
    if request.user.is_authenticated:
        return redirect('donorupdate')

    if request.method == 'GET':
        return render(request, 'otpverification.html')

    if request.method == 'POST':
        action = request.GET.get('action')
        if action == 'sendotp':
            contact_no = request.POST.get('contact_no')[-11:]
            try:
                user = User.objects.get(username=contact_no)
                if user:
                    error = "এই নাম্বার দিয়ে অন্য একটি একাউন্ট করা আছে, নতুন কোনো নাম্বার দিয়ে চেস্টা করুন "
                    context = {"error": error}
                    return render(request,'otpverification.html',context)

            except:
                pass
            contact_no = "88"+request.POST.get('contact_no')[-11:]
            # print(len(contact_no))
            
            if len(contact_no) != 13:
                context = {
                    'error' : 'আপনার মোবাইল নাম্বার সঠিক ভাবে টাইপ করুন । যেমন: 01712345678'
                }
                return render(request, 'otpverification.html',context)

            otp = random.randint(111111,999999)
                
            message = f"Your Verification OTP is {otp}"
            
            response = send_sms(contact_no,message)
            if response == None:
                context = {
                    'error' : 'Something Went Wrong'
                }
                return render(request, 'otpverification.html',context) 

            response = response.json()


            if response['ErrorCode'] == 0 and response['Data'][0]['MessageErrorDescription'] == 'Success':

                # print(response['ErrorCode'])
                # print(response['Data'][0]['MessageErrorDescription'])
                # print(type(response))

                context = {
                    'contact_no' : contact_no,
                    'otp' : otp,
                    'otpsent' : True,
                }

                return render(request,"otpverification.html",context) 
            else:
                context = {
                    'error' : 'আপনার মোবাইল নাম্বার সঠিক ভাবে টাইপ করুন । যেমন: 01712345678'
                }
                return render(request, 'otpverification.html',context)
        if action == 'otpverify':
            contact_no = request.POST.get('contact_no')
            otp = request.POST.get('otp')     
            inputotp = request.POST.get('inputotp')
            if inputotp == otp:

                contact_no = contact_no[2:]

                # set to session
                request.session['contact_no'] = contact_no

                context = {
                    'title': 'রক্তদাতা হিসেবে রেজিস্ট্রেশন করুন',
                    
                }
                return render(request, 'register.html', context)
            else:
                context = {
                    'otpError' : 'আপনার ভেরিফিকেশন কোডটি ভুল, পুনরায় সঠিক কোডটি বসান',
                    
                    'otp':inputotp,
                    'otpsent':True,
                }
                return render(request, 'otpverification.html',context)



def create_account(request):
    if request.method == 'POST':
        contact_no = request.session.get('contact_no')
       
        email = request.POST.get('email')
        name = request.POST.get('name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # print(contact_no, email, name, password1, password2)

        if password1 != password2:
            pass_error = "প্রথম পাসওয়ার্ড এর সাথে ২য় পাসওয়ার্ড এর মিল নেই। দুই ক্ষেত্রেই একই পাসওয়ার্ড ব্যাবহার করুন"
        
            context = {
                "pass_error" : pass_error,
                
            }
            return render(request, 'register.html', context)
        
        user = User.objects.create_user(contact_no,email,password1)
        user.first_name = name
        user.save()

        donor = Donor(user=user,contact_no = contact_no)
        donor.save()

        login(request,user)

        return redirect("donorupdate")

            


# def register(request):
#     if request.user.is_authenticated:
#         return redirect('donorupdate')

#     form = DonorRegistrationForm()
#     if request.method == 'POST':
#         form = DonorRegistrationForm(data=request.POST)
#         if form.is_valid():
#             user = form.save()
#             print(user)
#             donordata = Donor()
#             donordata.user = user
#             donordata.contact_no = user.username
#             donordata.save()
#             if user is not None:

#                 print("authenticated")
#                 login(request, user)

#                 print("logged in")

#                 return redirect('donorupdate')

#             return redirect('home')

#     context = {
#         'title': 'রক্তদাতা হিসেবে রেজিস্ট্রেশন করুন',
#         'form': form,
#     }
#     return render(request, 'register.html', context)


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



def blood_request_sms(contact_no):
    contact_no = "88"+contact_no
    message = "sent from request "
    response = send_sms(contact_no,message)
    response = response.json()
    # print(response)
    return response


@csrf_exempt
def request_blood(request):
    if request.is_ajax():
        donor_id = request.POST.get('id')
        # print(donor_id)
        donor = Donor.objects.get(id=donor_id)
        print(donor.contact_no)

        response = blood_request_sms(donor.contact_no)
        if response['ErrorCode'] == 0 and response['Data'][0]['MessageErrorDescription'] == 'Success':
            return JsonResponse({"success":True})
        else:
            return JsonResponse({"success":False})