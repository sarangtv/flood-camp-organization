
from django.urls import path
from .import  views
urlpatterns = [ 
    path('',views.displayhome,name='homepage'),
    path('singin_page',views.login_display,name='sign_in'),
    path('guest_registartion',views.guest_user_registration,name='guest_user_registration'),
    path('camp_registration',views.camp_organizer_registration,name='camp_organizer_registration'),
    path('admin_dashboard',views.admin_board,name='admin_dashboard'),
    path('camp_organizer_dashboard',views.camp_organizer_board,name='camp_organizer_dashboard'),
    path('camp_organizer__view_notification',views.camp_organizer_notification,name='camp_organizer_view_notification'),
    path('collector_dashboard',views.collector_board,name='collector_dashboard'),
    path('collector_view_notification',views.collector_notification,name='collector_view_notification'),
    path('guest_user_dashboard',views.guest_user_board,name='guest_user_dashboard'),
    path('police_dashboard',views.police_board,name='police_dashboard'),
    path('police_view_notification',views.view_notification,name='police_view_notification'),
    path('add_camp',views.add_camp,name='add_camp'),
    path('view_camp_details',views.view_camp_details,name='view_camp_details'),
    path('add_victim',views.add_victim,name='add_victim'),
    path('edit_victim',views.remove_victim,name='edit_victim'),
    path('add_requirements',views.add_requirements,name='add_requirements'),
    path('add_doctor',views.add_doctor,name='add_doctor'),
    path('add_medicine',views.add_medicine,name='add_medicine'),
    path('add_medical_req',views.add_medical_requirements,name='add_medical_req'),
    path('update_health_victim',views.update_health,name='victim_health_updates'),
    path('health_cordinator',views.health_cordinator,name='health_cordinator'),
    path('police_camp_view',views.camp_view_police,name='police_camp_view'),
    path('police_alert',views.police_alert,name='police_alert'),
    path('poilice_view_alert',views.alert_message_view,name='view_alert'),
    path('collector_view_camp',views.collector_view_camp,name='collector_view_camp'),
    path('collector_view_victim',views.collector_view_victim,name='collector_view_victim'),
    path('collector_view_donation',views.collector_view_donation,name='view_donations'),
    path('user_view_camp',views.user_view_camp,name='user_view_camp'),
    path('user_view_victim',views.user_view_victim,name='user_view_victim'),
    path('user_camp_requirements',views.user_view_requirements,name='user_view_camp_requirements'),
    path('user_camp_medrequirements',views.user_view_medical_requirements,name='user_view_camp_medrequirements'),
    path('user_view_warning',views.view_warning,name='user_view_warning'),
    path('guest_user_donation',views.pay_donation,name='user_donation'),
    path('guest_user_donation_msg',views.sucess_message),
    path('volunteer_registration',views.volunteer_register,name='volunteer_registration'),
    path('volunteer_dashboard',views.volunteer_board,name='volunteer_dashboard'),
    path('volunteer_update_req_status',views.update_req_status,name='req_update_status'),
    path('add_vechile',views.add_travel_facilities,name='add_vechile'),
    path('update_vechile_status',views.update_vechile_status,name='update_vechile_info'),
    path('approve_user',views.approve_users,name='approve_user'),
    path('approve_volunteers',views.approve_volunteers,name='approve_volunteers'),
    path('approve_camp_organizers',views.approve_camp_organizer,name='approve_camp_organizers'),
    path('add_flood_location',views.flood_area_update,name='add_flood_location'),
    path('volunteer_view_flood_area',views.view_flood_area,name='view_flood_location'),
    path('volunteer_view_notification',views.volunteer_notification,name='volunteer_view_notification'),
    path('flood_area_removal',views.remove_flood_location,name='location_removal'),
    path('eror', views.display_eror),
    

]
