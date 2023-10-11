from django import forms
from .models import *
from django.core.exceptions import ValidationError
import re






def phone_number_validator(value):
    if not re.compile(r'^[7-9]\d{9}$').match(value):
        raise ValidationError('This is Not a Valid Phone Number')
# login form

class login_form(forms.ModelForm):
    
    class Meta:
        model=login_table
        fields=['username','password']

# camp details

class add_camp_form(forms.ModelForm):

    class Meta:
        model=camp_details
        fields=['camp_name','location','phone','food_arrangements','camp_type','accomodation','bathroom_no']


# add victims

class victim_form(forms.ModelForm):

    class Meta:
        model=victim_details
        fields=['camp_name','victim_name','phone','location']


# add requirements

class requirements_form(forms.ModelForm):
    
    class Meta:
        model=requirement_table
        fields=['camp_name','requirements_details']


# add warning message by police

class warning_form(forms.ModelForm):

    class Meta:
        model=warning_table
        fields=['location','message']


# add vechile details

class vechile_form(forms.ModelForm):

    class Meta:
        model=vechile_info
        fields=['owner_name','vechile_type','location','phone']


# guest user registration 

class guest_user_registration_form(forms.ModelForm):

    class Meta:
        model=user_registered
        fields=['username','password','email','phone','name']


# volunteer Registration
class volunteer_registration_form(forms.ModelForm):
    
    class Meta:
        model=volunteer_registered
        fields=['username','password','email','phone','name']

# camp organizer registration

class camp_organizer_registration_form(forms.ModelForm):
    
    class Meta:
        model=camp_organizer_registered
        fields=['username','password','email','phone','name']


# location update form

class location_form(forms.ModelForm):
    
    class Meta:
        model=flood_area
        fields=['location','map_location']



class medicineform(forms.ModelForm):
    class Meta:
        model=medicine
        fields="__all__"


class doctorform(forms.ModelForm):
    phone = forms.CharField(validators=[phone_number_validator], required=True)
    class Meta:
        model=doctor
        fields="__all__"