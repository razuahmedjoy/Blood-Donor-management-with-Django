from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class suruKotha(models.Model):
    description = HTMLField(null=True, blank=True)


    def __str__(self):
        return f"Shurur Kotha"


class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=60,blank=True,null=True)
    address = models.CharField(max_length=250,blank=True,null=True)
    picture = models.ImageField(upload_to="volunteers/",blank=True,null=True)
    fb_link = models.CharField(max_length=200,blank=True,null=True)
    contact_no = models.CharField(max_length=13,blank=True,null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Mentor(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=60,blank=True,null=True)
    address = models.CharField(max_length=250,blank=True,null=True)
    picture = models.ImageField(upload_to="mentors/",blank=True,null=True)
    fb_link = models.CharField(max_length=200,blank=True,null=True)
    contact_no = models.CharField(max_length=13,blank=True,null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Adviser(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=60,blank=True,null=True)
    address = models.CharField(max_length=250,blank=True,null=True)
    picture = models.ImageField(upload_to="adviser/",blank=True,null=True)
    fb_link = models.CharField(max_length=200,blank=True,null=True)
    contact_no = models.CharField(max_length=13,blank=True,null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class shohojogi(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=100,null=True,blank=True)
    contact_no = models.CharField(max_length=50,blank=True,null=True)


    def __str__(self):
        return self.name

class BLog_Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Blog(models.Model):

    title = models.CharField(max_length=250)
    coverphoto = models.ImageField(upload_to="blogs/",blank=True,null=True)
    category = models.ForeignKey(BLog_Category,on_delete=models.CASCADE)
    description = HTMLField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class Donor(models.Model):
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
    STATUS = (
        ('active', 'active'),
        ('deactivate', 'deactivate'),
    )
    DISCTRICTS = (
        
        ('Chattogram','Chattogram'),
       
        
    )

    SUB_DISCTRICTS = (
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

    WARDS = (
        ('1','1'),
        ('2','2'),
        ('3','3'),
        ('4','4'),
        ('5','5'),
        ('6','6'),
        ('7','7'),
        ('8','8'),
        ('9','9'),
    )
    UNION = (
        ('চরতী','চরতী'),
        ('খাগরিয়া','খাগরিয়া'),
        ('নলুয়া','নলুয়া'),
        ('কাঞ্চনা','কাঞ্চনা'),
        ('অমিলাইশ','অমিলাইশ'),
        ('এওচিয়া','এওচিয়া'),
        ('মাদারশা','মাদারশা'),
        ('ঢেমশা','ঢেমশা'),
        ('পশ্চিম ঢেমশা','পশ্চিম ঢেমশা'),
        ('কেঁওচিয়া','কেঁওচিয়া'),
        ('কালিয়াইশ','কালিয়াইশ'),
        ('বাজালিয়া','বাজালিয়া'),
        ('পুরানগড়','পুরানগড়'),
        ('ছদাহা','ছদাহা'),
        ('সাতকানিয়া','সাতকানিয়া'),
        ('সোনাকানিয়া','সোনাকানিয়া'),
        ('সাতকানিয়া সদর','সাতকানিয়া সদর'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=100)
    blood_group = models.CharField(choices=GROUPS, max_length=10, blank=True)
    dob = models.DateField(blank=True, null=True)
    district = models.CharField(max_length=100,choices=DISCTRICTS, blank=True,null=True)
    sub_district = models.CharField(max_length=100,choices=SUB_DISCTRICTS, blank=True,null=True)
    ward_no = models.CharField(max_length=100,choices=WARDS, blank=True,null=True)
    union = models.CharField(max_length=100,choices=UNION, blank=True,null=True)
    address = models.CharField(max_length=250, blank=True)
    last_donated = models.DateField(blank=True, null=True)
    fb = models.URLField(blank=True)
    whatsapp = models.CharField(blank=True, max_length=15)
    status = models.CharField(
        max_length=10, choices=STATUS, default='deactivate')

    def __str__(self):
        return self.user.first_name + " (" + str(self.contact_no) + ")"

    def fullname(self):
        return self.user.first_name

    def email(self):
        return self.user.email

    def age(self):

        import datetime
        if (datetime.date.today() - self.dob):
            diff = str((datetime.date.today() - self.dob)/365)
            return diff[:2]
