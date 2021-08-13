from django.db import models
from django.contrib.auth.models import User

# Create your models here.


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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact_no = models.CharField(max_length=100)
    blood_group = models.CharField(choices=GROUPS, max_length=10, blank=True)
    dob = models.DateField(blank=True, null=True)
    district = models.CharField(max_length=100,choices=DISCTRICTS, blank=True)
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
