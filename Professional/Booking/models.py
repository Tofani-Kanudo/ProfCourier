from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class p_user(AbstractUser):
    pass
    origin=models.ForeignKey('origin',on_delete=models.CASCADE,blank=True)
    branches=models.ForeignKey('branch',on_delete=models.CASCADE,blank=True)
    admin=models.BooleanField(blank=True)
    class Meta:
        db_table=u'Prof_Users'
    def __str__(self):
        return self.username
class party(models.Model):
    number=models.CharField(max_length=13,null=True,unique=True,primary_key=True)
    reference=models.CharField(max_length=13,null=True,unique=False,blank=True)
    phone=models.CharField(max_length=13,null=True,unique=False,blank=True)
    name=models.CharField(max_length=40,null=True,blank=False)
    address1=models.CharField(max_length=500,null=True,blank=False)
    address2=models.CharField(max_length=500,null=True,blank=False)
    city=models.CharField(max_length=50,null=True,blank=False)
    email=models.EmailField(max_length=100,null=True,blank=True)
    gst=models.CharField(max_length=15,null=True,blank=True)
    company=models.CharField(max_length=100,null=True,blank=True)
    sur_price=models.ForeignKey('price',on_delete=models.CASCADE,blank=True,null=True,related_name='surface')
    air_price=models.ForeignKey('price',on_delete=models.CASCADE,blank=True,null=True,related_name='Air')
    class Meta:
        db_table=u'Party'
    def __str__(self):
        return self.number
class apod(models.Model):
    apod=models.CharField(max_length=11,null=True,unique=True,primary_key=True)
    p_user=models.ForeignKey(p_user,on_delete=models.CASCADE)
    class Meta:
        db_table=u'allocated_pod'
    def __str__(self):
        return self.apod
class branch(models.Model):
   branch=models.CharField(max_length=3,null=True,blank=False,primary_key=True)
   origin=models.ForeignKey('origin',on_delete=models.CASCADE)
   class Meta:
       db_table=u'Branches'
   def __str__(self):
       return self.branch
class origin(models.Model):
   origin=models.CharField(max_length=3,null=True,unique=False,primary_key=True)
   class Meta:
       db_table=u'Origin'
   def __str__(self):
       return self.origin
class book(models.Model):
   pod=models.CharField(max_length=11,null=True,unique=True,primary_key=True)
   booktype=models.CharField(max_length=6,null=True,blank=False)
   sender=models.ForeignKey(party,on_delete=models.CASCADE,related_name='sender')
   reciever=models.ForeignKey(party,on_delete=models.CASCADE,related_name='receiver')
   branch=models.CharField(max_length=3,null=True,blank=False)
   time=models.DateTimeField(auto_now_add=True,null=True)
   destination=models.CharField(max_length=15,null=True,blank=False)
   nop=models.IntegerField()
   weight=models.CharField(max_length=11,null=True)
   amount=models.CharField(max_length=11,null=True)
   value=models.CharField(max_length=11,null=True,blank=True)
   content=models.CharField(max_length=100,null=True,blank=True)
   p_user=models.ForeignKey(p_user,on_delete=models.CASCADE)
   class Meta:
       db_table=u'Booking'
   def __str__(self):
       return self.pod
class content(models.Model):
    content=models.CharField(max_length=1000)
    author=models.ForeignKey(p_user,on_delete=models.CASCADE)
    class Meta:
       db_table=u'Content'
    def __str__(self):
       return self.content
class price(models.Model):
    first_local=models.IntegerField(null=True)
    first_sau=models.IntegerField(null=True)
    first_guj=models.IntegerField(null=True)
    first_west=models.IntegerField(null=True)
    first_metro=models.IntegerField(null=True)
    first_ROI=models.IntegerField(null=True)
    first_spec=models.IntegerField(null=True)
    local=models.IntegerField()
    sau=models.IntegerField()
    guj=models.IntegerField()
    west=models.IntegerField()
    metro=models.IntegerField()
    ROI=models.IntegerField()
    spec=models.IntegerField()
    class Meta:
       db_table=u'Price'
    def __str__(self):
       return str(self.first_local)
class location(models.Model):
    pincode=models.IntegerField(primary_key=True)
    district=models.CharField(max_length=40,null=True,blank=False)
    state=models.CharField(max_length=40,null=True,blank=False)
    class Meta:
       db_table=u'Location'
    def __str__(self):
       return self.district