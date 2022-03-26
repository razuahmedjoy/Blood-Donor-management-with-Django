from django import forms
from django.forms import DateField
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Donor


class DonorRegistrationForm(UserCreationForm):
  
    username = forms.CharField(required=True, label="আপনার কন্টাক্ট নাম্বার", widget=forms.TextInput(
        attrs={'placeholder': '01XXXXXXXXXX'}))
    email = forms.CharField(required=True, label="আপনার ইমেইল লিখুন", widget=forms.TextInput(
        attrs={'placeholder': 'your email address'}))

    first_name = forms.CharField(required=True, label="আপনার নাম", widget=forms.TextInput(
        attrs={'placeholder': 'Your full name here'}))

    password1 = forms.CharField(
        required=True,
        label="একটি পাসওয়ার্ড সেট করুন",
        widget=forms.PasswordInput(attrs={
            'placeholder': "Enter Password",
        })
    )
    password2 = forms.CharField(
        required=True,
        label="পুনরায় একই পাসওয়ার্ড লিখুন",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': "Enter Password again!",
            }
        ),
    )

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'password1', 'password2')


class DonorUpdateform(forms.ModelForm):
    GROUPS = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
    DISCTRICTS = (
       
        ('Chattogram','Chattogram'),
    
    )
    SUB_DISTRICTS = (
        ('সাতকানিয়া', 'সাতকানিয়া'),
        ('সীতাকুন্ড', 'সীতাকুন্ড'),
        ('মীরসরাই', 'মীরসরাই'),
        ('পটিয়া', 'পটিয়া'),
        ('পটিয়া', 'পটিয়া'),
        ('সন্দ্বীপ', 'সন্দ্বীপ'),
        ('বাঁশখালী', 'বাঁশখালী'),
        ('বোয়ালখালী', 'বোয়ালখালী'),
        ('আনোয়ারা', 'আনোয়ারা'),
        ('চন্দনাইশ', 'চন্দনাইশ'),
        ('রাঙ্গুনিয়া', 'রাঙ্গুনিয়া'),
        ('লোহাগাড়া', 'লোহাগাড়া'),
        ('হাটহাজারী', 'হাটহাজারী'),
        ('ফটিকছড়ি', 'ফটিকছড়ি'),
        ('রাউজান', 'রাউজান'),
        ('কর্ণফুলী', 'কর্ণফুলী'),
    )

  
        
    contact_no = forms.CharField(
        required=True, label="আপনার নাম্বার")
    blood_group = forms.ChoiceField(
        required=True, label="রক্তের গ্রুপ", choices=GROUPS)

    dob = forms.DateField(
        required=True, label="জন্মতারিখ", widget=forms.DateInput(format=('%d-%m-%Y'), attrs={'type': 'date'}))
    # last_donated = forms.CharField(
    #     required=False, label="শেষ কবে রক্ত দিয়েছেন ( না দিয়ে থাকলে কিছু দিতে হবেনা এখানে ) ", widget=forms.DateInput(format=('%d-%m-%Y'), attrs={'type': 'date'}))
    district = forms.ChoiceField(
        required=True, label="আপনার জেলা শহরের নাম", choices=DISCTRICTS)
    sub_district = forms.ChoiceField(
        required=True, label="আপনার উপজেলার নাম", choices=SUB_DISTRICTS)
    
    address = forms.CharField(
        required=True, label="আপনার এলাকা/মহল্লার নাম", widget=forms.DateInput(attrs={'placeholder': 'Street or Area'}))
    fb = forms.CharField(
        required=False, label="আপনার ফেসবুক আইডি লিংক ( যদি থাকে )", widget=forms.DateInput(attrs={'placeholder': 'www.facebook.com/youridusername'}))

    class Meta:
        model = Donor
        exclude = ('user', 'status','last_donated')
