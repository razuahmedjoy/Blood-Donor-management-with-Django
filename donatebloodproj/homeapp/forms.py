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
        ('Comilla','Comilla'),
        ('Feni','Feni'),
        ('Brahmanbaria','Brahmanbaria'),
        ('Rangamati','Rangamati'),
        ('Noakhali','Noakhali'),
        ('Chandpur','Chandpur'),
        ('Lakshmipur','Lakshmipur'),
        ('Chattogram','Chattogram'),
        ('Coxsbazar','Coxsbazar'),
        ('Khagrachhari','Khagrachhari'),
        ('Bandarban','Bandarban'),
        ('Sirajganj','Sirajganj'),
        ('Pabna','Pabna'),
        ('Bogura','Bogura'),
        ('Rajshahi','Rajshahi'),
        ('Natore','Natore'),
        ('Joypurhat','Joypurhat'),
        ('Chapainawabganj','Chapainawabganj'),
        ('Naogaon','Naogaon'),
        ('Jashore','Jashore'),
        ('Satkhira','Satkhira'),
        ('Meherpur','Meherpur'),
        ('Narail','Narail'),
        ('Chuadanga','Chuadanga'),
        ('Kushtia','Kushtia'),
        ('Magura','Magura'),
        ('Khulna','Khulna'),
        ('Bagerhat','Bagerhat'),
        ('Jhenaidah','Jhenaidah'),
        ('Jhalakathi','Jhalakathi'),
        ('Patuakhali','Patuakhali'),
        ('Pirojpur','Pirojpur'),
        ('Barisal','Barisal'),
        ('Bhola','Bhola'),
        ('Barguna','Barguna'),
        ('Sylhet','Sylhet'),
        ('Moulvibazar','Moulvibazar'),
        ('Habiganj','Habiganj'),
        ('Sunamganj','Sunamganj'),
        ('Narsingdi','Narsingdi'),
        ('Gazipur','Gazipur'),
        ('Shariatpur','Shariatpur'),
        ('Narayanganj','Narayanganj'),
        ('Tangail','Tangail'),
        ('Kishoreganj','Kishoreganj'),
        ('Manikganj','Manikganj'),
        ('Dhaka','Dhaka'),
        ('Munshiganj','Munshiganj'),
        ('Rajbari','Rajbari'),
        ('Madaripur','Madaripur'),
        ('Gopalganj','Gopalganj'),
        ('Faridpur','Faridpur'),
        ('Panchagarh','Panchagarh'),
        ('Dinajpur','Dinajpur'),
        ('Lalmonirhat','Lalmonirhat'),
        ('Nilphamari','Nilphamari'),
        ('Thakurgaon','Thakurgaon'),
        ('Rangpur','Rangpur'),
        ('Kurigram','Kurigram'),
        ('Sherpur','Sherpur'),
        ('Mymensingh','Mymensingh'),
        ('Jamalpur','Jamalpur'),
        ('Netrokona','Netrokona'),
        
    )
    contact_no = forms.CharField(
        required=True, label="আপনার নাম্বার")
    blood_group = forms.ChoiceField(
        required=True, label="রক্তের গ্রুপ", choices=GROUPS)

    dob = forms.DateField(
        required=True, label="জন্মতারিখ", widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}))
    last_donated = forms.CharField(
        required=False, label="শেষ কবে রক্ত দিয়েছেন ( না দিয়ে থাকলে কিছু দিতে হবেনা এখানে ) ", widget=forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}))
    district = forms.ChoiceField(
        required=True, label="আপনার জেলা শহরের নাম", choices=DISCTRICTS)
    address = forms.CharField(
        required=True, label="আপনার এলাকা/মহল্লা/উপজেলা যেকোনো একটি দিন", widget=forms.DateInput(attrs={'placeholder': 'Street or Area'}))
    fb = forms.CharField(
        required=False, label="আপনার ফেসবুক আইডি লিংক ( যদি থাকে )", widget=forms.DateInput(attrs={'placeholder': 'www.facebook.com/youridusername'}))

    class Meta:
        model = Donor
        exclude = ('user', 'status')
