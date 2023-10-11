from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

#homepage display

def displayhome(request):
    
    return render(request,'index.html')

#login page display

def login_display(request):
    if request.method == 'POST':
        form=login_form(request.POST)
        username=request.POST.get("username")
        passwd=request.POST.get("password")

        if registered.objects.filter(username=username,password=passwd).exists():
            obj=registered.objects.get(username=username)
            if form.is_valid():
                
                if obj.role == 'police' and obj.status == 'Approved':
                      form.save()
                      return render(request,'Police.html')
                elif obj.role == 'admin' and obj.status == 'Approved':
                    form.save()
                    return render(request,'admin_page.html') 
                elif obj.role == 'collector' and obj.status == 'Approved':
                    form.save()
                    return render(request,'Collector.html')
                elif obj.role=='health' and obj.status=='Approved':
                    form.save()
                    return render(request,'health_cordinator.html')
                else:
                    return render(request,'error.html')
        elif volunteer_registered.objects.filter(username=username,password=passwd).exists(): 
            obj=volunteer_registered.objects.get(username=username)
            if form.is_valid():
                if obj.status == 'Approved':
                    form.save()
                    return render(request,'volunteer.html')
                else:
                    return render(request,'error.html')
        elif camp_organizer_registered.objects.filter(username=username,password=passwd).exists(): 
            obj=camp_organizer_registered.objects.get(username=username)
            if form.is_valid():
                if obj.status == 'Approved':
                    form.save()
                    return render(request,'Camp_oraginizer.html')
                else:
                    return render(request,'error.html')
        elif user_registered.objects.filter(username=username,password=passwd).exists():
            obj=user_registered.objects.get(username=username)
            if form.is_valid():
                if obj.status == 'Approved':
                    form.save()
                    return render(request,'Guest_users.html')
                else:
                    return render(request,'error.html') 
        else :
            return render(request,'error.html')
    else:
        form=login_form()
        

    return render(request,'signin.html',{'form':form})
    
# eror display 
def display_eror(request):

    return render(request,'error.html')
# guest user registration

def guest_user_registration(request):

    if request.method == 'POST':
        form=guest_user_registration_form(request.POST)
        name=request.POST.get("name")
        if not user_registered.objects.filter(name=name, role='guest_user').exists():

            if form.is_valid():
                obj=form.save(commit=True)
                obj.role='guest_user'
                obj.save()
                return render(request,'index.html')
        else:
            messages.error(request, 'You have been already registered.')
    else:
        form=guest_user_registration_form()


    return render(request,'guest_registration_form.html')

# camp organizer registration

def camp_organizer_registration(request):

    if request.method == 'POST':
        form=camp_organizer_registration_form(request.POST)
        name=request.POST.get("name")
        if not camp_organizer_registered.objects.filter(name=name, role='camp_organizer').exists():
            if form.is_valid():
                obj=form.save(commit=True)
                obj.role='camp_organizer'
                obj.save()
                return render(request,'index.html')
        else:
            messages.error(request, 'You have been already registered.')
    else:
        form=camp_organizer_registration_form()


    return render(request,'camp_organizer_registration_form.html')


# load camp organizer dash board

def camp_organizer_board(request):

    obj1=requirement_table.objects.filter(status='Delievered').order_by('-id')
    obj2=warning_table.objects.all().order_by('-id')

    count=0

    for x in obj1:
        count=count+1
    
    for y in obj2:
        count=count+1



    return render(request,'Camp_oraginizer.html',{'requirement':obj1,'warning':obj2,'count':count})


# add new camp
def add_camp(request):
    
    
   
    if request.method == 'POST':
        form=add_camp_form(request.POST)
        name=request.POST.get("camp_name")
        
        camp_location=request.POST.get("location")
        if not camp_details.objects.filter(camp_name=name,location=camp_location).exists():
            if form.is_valid():
                form.save()
                return render(request,'Camp_oraginizer.html')
        else:
            messages.error(request, 'camp already added.')   
    else:
        form=add_camp_form()

    
    
    return render(request,'add_camp_form.html',{'form':form})

# view camp details
def view_camp_details(request):
    obj=camp_details.objects.all()
    obj1=requirement_table.objects.filter(status='Delievered').order_by('-id')
    obj2=warning_table.objects.all().order_by('-id')

    count=0

    for x in obj1:
        count=count+1
    
    for y in obj2:
        count=count+1
    
    req_id=request.POST.get("id")
    
    

    try:
        update_obj=camp_details.objects.get(id=req_id)
    except camp_details.DoesNotExist:
        update_obj=None

    
    #print(req_id)
    
    #update_obj=registered.objects.get(id=req_id)
    
   # print(update_obj)
    if request.method == 'POST':
        update_obj.delete()
    
    return render(request,'Camp_details.html',{'camp_details':obj,'requirement':obj1,'warning':obj2,'count':count})




# add victims
def add_victim(request):
    if request.method == 'POST':
        form=victim_form(request.POST)
        name=request.POST.get("victim_name")
        camp=request.POST.get("camp_name")
        if not victim_details.objects.filter(victim_name=name, camp_name=camp).exists():
            if form.is_valid():
                form.save()
                return render(request,'Camp_oraginizer.html')
        else:
             messages.error(request, 'Victim has already added.')
    else:
        form=victim_form()
    obj=camp_details.objects.all()
    return render(request,'add_victim.html',{'camp_obj':obj})

# remove victim
def remove_victim(request):
    obj=victim_details.objects.all()
    obj1=requirement_table.objects.filter(status='Delievered').order_by('-id')
    obj2=warning_table.objects.all().order_by('-id')

    count=0

    for x in obj1:
        count=count+1
    
    for y in obj2:
        count=count+1
    
    
    req_id=request.POST.get("id")
    
    

    try:
       update_obj=victim_details.objects.get(id=req_id)
    except victim_details.DoesNotExist:
        update_obj=None

    
    #print(req_id)
    
    #update_obj=registered.objects.get(id=req_id)
    
   # print(update_obj)
    if request.method == 'POST':
        update_obj.delete()

    return render(request,'edit_victim.html',{'victim_details':obj,'requirement':obj1,'warning':obj2,'count':count})



# add camp requirements
def add_requirements(request):
    obj=camp_details.objects.all()
    if request.method == 'POST':
        form=requirements_form(request.POST)
        if form.is_valid():
            obj2=form.save(commit=True)
            obj2.requirement_type='other requirements'
            obj2.save()
            return render(request,'Camp_oraginizer.html')
    else:
        form=requirements_form()
    return render(request,'add_requirements.html',{'camp_obj':obj})

# add medical requirements
def add_medical_requirements(request):
    obj=camp_details.objects.all()
    if request.method == 'POST':
        form=requirements_form(request.POST)
        if form.is_valid():
            obj3=form.save(commit=True)
            obj3.requirement_type='medical requirements'
            obj3.save()
            return render(request,'Camp_oraginizer.html')
    else:
        form=requirements_form()
    return render(request,'add_requirements.html',{'camp_obj':obj})

# view notification

def camp_organizer_notification(request):

    obj1=requirement_table.objects.filter(status='Delievered').order_by('-id')
    obj2=warning_table.objects.all().order_by('-id')

    return render(request,'Camp_organizer_view_notification.html',{'requirement':obj1,'warning':obj2})

# update health condition of victim
def update_health(request):

    obj=victim_details.objects.all()

    req_id=request.POST.get("id")
    obj1=requirement_table.objects.filter(status='Delievered').order_by('-id')
    obj2=warning_table.objects.all().order_by('-id')

    count=0

    for x in obj1:
        count=count+1
    
    for y in obj2:
        count=count+1
    
    

    try:
        update_obj=victim_details.objects.get(id=req_id)
    except victim_details.DoesNotExist:
        update_obj=None

    if request.method == 'POST':
        status_update=request.POST.get("update")
        update_obj.health_status=status_update
        update_obj.save()

    return render(request,'Camp_org_update_victim_health.html',{'health_updates':obj,'requirement':obj1,'warning':obj2,'count':count})

def health_cordinator(request):
    return render(request,'health_cordinator.html')

def add_doctor(request):
    form = doctorform()
    if request.method=='POST':
        form=doctorform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "added successfully")
            return redirect('add_doctor')
    return render(request,'add_doctor.html',{'form':form})

def add_medicine(request):
    form = medicineform()
    if request.method=='POST':
        form=medicineform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "added successfully")
            return redirect('add_medicine')
    return render(request,'add_medicine.html',{'form':form})
# load admin dash board

def admin_board(request):

    return render(request,'admin_page.html')

# approve users
 
def approve_users(request):

    #obj=registered.objects.all()
    #obj2=camp_organizer_registered.objects.all()
    #obj3=volunteer_registered.objects.all()
    obj=user_registered.objects.all()
    req_id=request.POST.get("id")
    
    

    try:
        update_obj=user_registered.objects.get(id=req_id)
        #elif volunteer_registered.objects.filter(id=req_id).exists():
            #update_obj=volunteer_registered.objects.get(id=req_id)
        #else:
            #update_obj=camp_organizer_registered.objects.get(id=req_id)
            

        
    except user_registered.DoesNotExist:
        update_obj=None

    
    #print(req_id)
    
    #update_obj=registered.objects.get(id=req_id)
    
   # print(update_obj)
    
    if request.method == 'POST':
       status_update=request.POST.get("update")
       update_obj.status=status_update
       update_obj.save()
    

    return render(request,'admin_approve_request.html',{'user_details':obj})

# approve volunteers
 
def approve_volunteers(request):

    #obj=registered.objects.all()
    #obj2=camp_organizer_registered.objects.all()
    #obj3=volunteer_registered.objects.all()
    obj=volunteer_registered.objects.all()
    req_id=request.POST.get("id")
    
    

    try:
        update_obj=volunteer_registered.objects.get(id=req_id)
        #elif volunteer_registered.objects.filter(id=req_id).exists():
            #update_obj=volunteer_registered.objects.get(id=req_id)
        #else:
            #update_obj=camp_organizer_registered.objects.get(id=req_id)
            

        
    except volunteer_registered.DoesNotExist:
        update_obj=None

    
    #print(req_id)
    
    #update_obj=registered.objects.get(id=req_id)
    
   # print(update_obj)
    
    if request.method == 'POST':
       status_update=request.POST.get("update")
       update_obj.status=status_update
       update_obj.save()
    

    return render(request,'admin_approve_volunteer_request.html',{'volunteer_details':obj})

# approve camp organizer
 
def approve_camp_organizer(request):

    #obj=registered.objects.all()
    #obj2=camp_organizer_registered.objects.all()
    #obj3=volunteer_registered.objects.all()
    obj=camp_organizer_registered.objects.all()
    req_id=request.POST.get("id")
    
    

    try:
        update_obj=camp_organizer_registered.objects.get(id=req_id)
        #elif volunteer_registered.objects.filter(id=req_id).exists():
            #update_obj=volunteer_registered.objects.get(id=req_id)
        #else:
            #update_obj=camp_organizer_registered.objects.get(id=req_id)
            

        
    except camp_organizer_registered.DoesNotExist:
        update_obj=None

    
    #print(req_id)
    
    #update_obj=registered.objects.get(id=req_id)
    
   # print(update_obj)
    
    if request.method == 'POST':
       status_update=request.POST.get("update")
       update_obj.status=status_update
       update_obj.save()
    

    return render(request,'admin_approve_camp_org_request.html',{'camp_organizer_details':obj})

# add flood effected area

def flood_area_update(request):

    if request.method == 'POST':
        form=location_form(request.POST)
        
        if form.is_valid():
            form.save()
            return render(request,'admin_page.html')
    else:
        form=location_form()

    return render(request,'add_flood_location.html')


# remove flood location

def remove_flood_location(request):
    
    obj=flood_area.objects.all()
    req_id=request.POST.get("id")
    
    

    try:
        update_obj=flood_area.objects.get(id=req_id)
    except flood_area.DoesNotExist:
        update_obj=None

    
    #print(req_id)
    
    #update_obj=registered.objects.get(id=req_id)
    
   # print(update_obj)
    if request.method == 'POST':
        update_obj.delete()
    
    

    return render(request,'admin_remove_location.html',{'location_details':obj})


# load collector dash board

def collector_board(request):

    obj1=camp_details.objects.all().order_by('-id')
    obj2=requirement_table.objects.filter(status='').order_by('-id')
    obj3=flood_area.objects.all().order_by('-id')

    count=0

    for x in obj1:
        count=count+1
    for y in obj2:
        count=count+1
    for z in obj3:
        count=count+1
    

    return render(request,'Collector.html',{'camp':obj1,'requirement':obj2,'area':obj3,'count':count})

# collector view notification

def collector_notification(request):

    obj1=camp_details.objects.all().order_by('-id')
    obj2=requirement_table.objects.filter(status='').order_by('-id')
    obj3=flood_area.objects.all().order_by('-id')

    return render(request,'collector_view_notification.html',{'camp':obj1,'requirement':obj2,'area':obj3})


# collector view camp details

def collector_view_camp(request):

    obj1=camp_details.objects.all().order_by('-id')
    obj2=requirement_table.objects.filter(status='').order_by('-id')
    obj3=flood_area.objects.all().order_by('-id')

    count=0

    for x in obj1:
        count=count+1
    for y in obj2:
        count=count+1
    for z in obj3:
        count=count+1

    obj=camp_details.objects.all()

    return render(request,'Collector_view_camp.html',{'camp_details':obj,'camp':obj1,'requirement':obj2,'area':obj3,'count':count})

# collector view victim details

def collector_view_victim(request):

    obj= victim_details.objects.all()
    obj1=camp_details.objects.all().order_by('-id')
    obj2=requirement_table.objects.filter(status='').order_by('-id')
    obj3=flood_area.objects.all().order_by('-id')

    count=0

    for x in obj1:
        count=count+1
    for y in obj2:
        count=count+1
    for z in obj3:
        count=count+1

   

    return render(request,'Collector_view_victim.html',{'victim_details':obj,'camp':obj1,'requirement':obj2,'area':obj3,'count':count})


# collector view donations from user

def collector_view_donation(request):

    obj=user_donation.objects.all().order_by('-id')
    obj1=camp_details.objects.all().order_by('-id')
    obj2=requirement_table.objects.filter(status='').order_by('-id')
    obj3=flood_area.objects.all().order_by('-id')

    count=0

    for x in obj1:
        count=count+1
    for y in obj2:
        count=count+1
    for z in obj3:
        count=count+1

    return render(request,'Collector_view_donation.html',{'donation_details':obj,'camp':obj1,'requirement':obj2,'area':obj3,'count':count})




# load guest user dash board

def guest_user_board(request):

    obj=warning_table.objects.all().order_by('-id')
    count=0

    for i in obj:
        count=count+1

    return render(request,'Guest_users.html',{'warning_details':obj,'warning_count':count})

# guest user view camp details

def user_view_camp(request):

   obj=camp_details.objects.all()
   obj2=warning_table.objects.all().order_by('-id')
   count=0
   
   for i in obj2:
       count=count+1

   return render(request,'Guest_users_camp_view.html',{'camp_details':obj,'warning':obj2,'count':count})

# guest user view victim details

def user_view_victim(request):

    obj= victim_details.objects.all()
    obj2=warning_table.objects.all().order_by('-id')
    count=0
    for i in obj2:
       count=count+1

    return render(request,'Guest_users_view_victim.html',{'victim_details':obj,'warning':obj2,'count':count})

# guest user view camp requirements

def user_view_requirements(request):

    obj=requirement_table.objects.filter(requirement_type='other requirements')
    obj2=warning_table.objects.all().order_by('-id')
    count=0
    for i in obj2:
       count=count+1

    return render(request,'Guest_users_view_requirements.html',{'requirements':obj,'warning':obj2,'count':count})

# guest user view camp  medical requirements

def user_view_medical_requirements(request):

    obj=requirement_table.objects.filter(requirement_type='medical requirements')
    obj2=warning_table.objects.all().order_by('-id')
    count=0
    for i in obj2:
       count=count+1

    return render(request,'Guest_users_view_Medrequirements.html',{'requirements':obj,'warning':obj2,'count':count})

# guest user view warning
def view_warning(request):
    obj=warning_table.objects.all().order_by('-id')

    return render(request,'Guest_view_warning.html',{'warning':obj})

# guset user pay donation

def pay_donation(request):

    if request.method == 'POST':
        name=request.POST.get("username")
        amount=request.POST.get("fund_amount")
        user_donation(name=name,amount=amount).save()
        return render(request,'guest_user_payment_sucess.html')

    return render(request,'guest_user_payment.html')

# sucess page
def sucess_message(request):

    return render(request,'guest_user_payment_sucess.html')


# load police police dash board

def police_board(request):

    obj1=flood_area.objects.all().order_by('-id')
    obj2=camp_details.objects.all().order_by('-id')

    count=0

    for x in obj1:
        count=count+1
    
    for y in obj2:
        count=count+1

    return render(request,'Police.html',{'flood_area':obj1,'camp_details':obj2,'count':count})

# view camp details for police

def camp_view_police(request):

    obj=camp_details.objects.all()
    obj1=flood_area.objects.all().order_by('-id')
    obj2=camp_details.objects.all().order_by('-id')

    count=0

    for x in obj1:
        count=count+1
    
    for y in obj2:
        count=count+1

    return render(request,'Police_view_camp.html',{'camp_details':obj,'flood_area':obj1,'camp_details_print':obj2,'count':count})

# alert message from police

def police_alert(request):

    if request.method == 'POST':
        form=warning_form(request.POST)

        if form.is_valid():
            form.save()
            return render(request,'Police.html')
    else:
        form=warning_form()

    return render(request,'Police_alerts.html')

# alert message view
def alert_message_view(request):

    obj=warning_table.objects.all()
    obj1=flood_area.objects.all().order_by('-id')
    obj2=camp_details.objects.all().order_by('-id')

    count=0

    for x in obj1:
        count=count+1
    
    for y in obj2:
        count=count+1
    
    
    req_id=request.POST.get("id")
    
    

    try:
        update_obj=warning_table.objects.get(id=req_id)
    except warning_table.DoesNotExist:
        update_obj=None

    
    #print(req_id)
    
    #update_obj=registered.objects.get(id=req_id)
    
   # print(update_obj)
    if request.method == 'POST':
        update_obj.delete()
    

    return render(request,'Police_view_warning.html',{'warning_details':obj,'flood_area':obj1,'camp_details':obj2,'count':count})


# view notification

def view_notification(request):

    obj1=flood_area.objects.all().order_by('-id')
    obj2=camp_details.objects.all().order_by('-id')

    return render(request,'Police_view_notification.html',{'flood_area':obj1,'camp_details':obj2})

# volunteer regsitration page

def volunteer_register(request):

    if request.method == 'POST':
        form=volunteer_registration_form(request.POST)
        name=request.POST.get("name")
        if not volunteer_registered.objects.filter(name=name, role='volunteer').exists():
            if form.is_valid():
                 obj=form.save(commit=True)
                 obj.role='volunteer'
                 obj.save()
                 
                 return render(request,'index.html')
        else:
            messages.error(request, 'You have been already registered.')
    else:
        form=volunteer_registration_form()
        
            

    return render(request,'Volunteer_registration_form.html',{'form':form})


# load volunteer dash board

def volunteer_board(request):

    obj1=requirement_table.objects.filter(status='').order_by('-id')
    obj2=camp_details.objects.all().order_by('-id')
    count=0
    for x in obj1:
        count=count+1
    for y in obj2:
        count=count+1

    return render(request,'volunteer.html',{'camp':obj2,'requirement':obj1,'count':count})


#  volunteer view notifications

def volunteer_notification(request):

    obj1=requirement_table.objects.filter(status='').order_by('-id')
    obj2=camp_details.objects.all().order_by('-id')

    return render(request,'volunteer_view_notification.html',{'camp':obj2,'requirement':obj1})

# update requirements status

def update_req_status(request):

    obj=requirement_table.objects.all()
    req_id=request.POST.get("id")

    obj1=requirement_table.objects.filter(status='').order_by('-id')
    obj2=camp_details.objects.all().order_by('-id')
    count=0
    for x in obj1:
        count=count+1
    for y in obj2:
        count=count+1
    
   # print(req_id)
    
    #update_obj=requirement_table.objects.get(id=req_id)
    try:
        update_obj=requirement_table.objects.get(id=req_id)
    except requirement_table.DoesNotExist:
        update_obj=None
    
   # print(update_obj)
    
    if request.method == 'POST':
       status_update=request.POST.get("update")
       update_obj.status=status_update
       update_obj.save()
    

    return render(request,'volunteer_view_requirement_updates.html',{'requirements':obj,'camp':obj2,'requirement':obj1,'count':count})


# add travel facilities

def add_travel_facilities(request):

    if request.method == 'POST':
        form=vechile_form(request.POST)
        name=request.POST.get("owner_name")
        location=request.POST.get("location")
        if not vechile_info.objects.filter(owner_name=name, location=location).exists():
            if form.is_valid():
                form.save()
                return render(request,'volunteer.html')
        else:
            messages.error(request, ' already registered.')
    else:
        form=vechile_form()

    return render(request,'add_travel-vechile.html')


# update vechile status 

def update_vechile_status(request):

    obj=vechile_info.objects.all()
    req_id=request.POST.get("id")
    #print(req_id)
    #update_obj=vechile_info.objects.get(id=req_id)
    obj1=requirement_table.objects.filter(status='').order_by('-id')
    obj2=camp_details.objects.all().order_by('-id')
    count=0
    for x in obj1:
        count=count+1
    for y in obj2:
        count=count+1
    

    try:
        update_obj=vechile_info.objects.get(id=req_id)
    except vechile_info.DoesNotExist:
        update_obj=None

    if request.method == 'POST':
        status_update=request.POST.get("update")
        update_obj.status=status_update
        update_obj.save()

    return render(request,'vechile_updates.html',{'vechile_details':obj,'camp':obj2,'requirement':obj1,'count':count})


# flood area  map

def view_flood_area(request):
    
    obj=flood_area.objects.all()

    return render(request,'view_flood_area.html',{'map_details':obj})

