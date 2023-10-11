from django.db import models

# Create your models here.

#  register table
class registered(models.Model):
    name=models.CharField(max_length=250)
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    phone=models.CharField(max_length=250)
    role=models.CharField(max_length=250)
    status=models.CharField(max_length=250)

#  user register table
class user_registered(models.Model):
    name=models.CharField(max_length=250)
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    phone=models.CharField(max_length=250)
    role=models.CharField(max_length=250)
    status=models.CharField(max_length=250)

#  volunteer register table
class volunteer_registered(models.Model):
    name=models.CharField(max_length=250)
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    phone=models.CharField(max_length=250)
    role=models.CharField(max_length=250)
    status=models.CharField(max_length=250)

#  camp organizer register table
class camp_organizer_registered(models.Model):
    name=models.CharField(max_length=250)
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    phone=models.CharField(max_length=250)
    role=models.CharField(max_length=250)
    status=models.CharField(max_length=250)




# login table
class login_table(models.Model):
    username=models.CharField(max_length=250)
    password=models.CharField(max_length=250)
    

# camp_details table

class camp_details(models.Model):
    camp_name=models.CharField(max_length=250)
    location=models.CharField(max_length=250)
    phone=models.CharField(max_length=10)
    accomodation=models.IntegerField()
    bathroom_no=models.IntegerField()
    camp_type=models.CharField(max_length=250)
    food_arrangements=models.CharField(max_length=250)

# victim details

class victim_details(models.Model):
    camp_name=models.CharField(max_length=250)
    victim_name=models.CharField(max_length=250)
    phone=models.CharField(max_length=10)
    location=models.CharField(max_length=250)
    health_status=models.CharField(max_length=250)


# requirements table 

class requirement_table(models.Model):
    camp_name=models.CharField(max_length=250)
    requirements_details=models.CharField(max_length=1000)
    requirement_type=models.CharField(max_length=250)
    status=models.CharField(max_length=250)



# warning table

class warning_table(models.Model):
    location=models.CharField(max_length=250)
    message=models.CharField(max_length=250)


# vechile details

class vechile_info(models.Model):
    owner_name=models.CharField(max_length=250)
    vechile_type=models.CharField(max_length=250)
    location=models.CharField(max_length=250)
    phone=models.CharField(max_length=10)
    status=models.CharField(max_length=100)


# details about flood effected area

class flood_area(models.Model):

    location=models.CharField(max_length=250)
    map_location=models.CharField(max_length=1000)

# user donation 

class user_donation(models.Model):

    name=models.CharField(max_length=500)
    amount=models.IntegerField()


class medicine(models.Model):
    name=models.CharField(max_length=200)
    stock = models.IntegerField(default=0)


class doctor(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)