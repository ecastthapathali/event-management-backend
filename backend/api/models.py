from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import UserManager
from django.contrib.auth.models import Group, Permission

class UserData(AbstractBaseUser, PermissionsMixin):
    FACULTY_CHOICES = (
        ('BEI', 'Electronics, Communication, and Information Engineering'),
        ('BCT', 'Computer Engineering'),
        ('BCE', 'Civil Engineering'),
        ('BEE', 'Electrical Engineering'),
        ('BME', 'Mechanical Engineering'),
        ('BAR', 'Architecture'),
        ('BAE', 'Automobile Engineering'),
        ('BIE', 'Industrial Engineering'),
        ('BGE', 'Geomatics Engineering'),
        ('BAGE', 'Agricultural Engineering'),
        ('BCHE', 'Chemical Engineering'),
    )
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=10)
    campus_name = models.CharField(max_length=250)
    faculty = models.CharField(max_length=10, choices=FACULTY_CHOICES, default='BEI')
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    timestamp = models.DateTimeField(default=timezone.now)
    
    objects = UserManager()
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    groups = models.ManyToManyField(Group, related_name='custom_user_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='custom_user_permissions_set', blank=True)
    
    def __str__(self):
        return f"Name : {self.name} Email : {self.email}"

class EventModel(models.Model):
    organizer_id = models.ForeignKey(UserData, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=500)
    post = models.ImageField(upload_to="event_post/")
    location = models.TextField()
    event_time = models.TimeField()
    event_date = models.DateField()
    
    def __str__(self):
        return self.event_name

class EventReg(models.Model):
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE)  
    participant = models.ForeignKey(UserData, on_delete=models.CASCADE) 
    reg_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.participant.name} registered for {self.event.event_name}"

class Participants(models.Model):
    event_reg = models.OneToOneField(EventReg, on_delete=models.CASCADE)
    class_link = models.TextField()
    certificate_sent = models.BooleanField(default=False)
    certificate_sent_on = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"Name: {self.event_reg.participant.name} Event: {self.event_reg.event.event_name}"

class DigitalCertificate(models.Model):
    cert_id = models.OneToOneField(Participants, on_delete=models.CASCADE)
    sent_on = models.DateTimeField(blank=True, null=True)
    certificate_url = models.CharField(max_length=300)
    
    def __str__(self):
        return self.cert_id.event_reg.participant.name
