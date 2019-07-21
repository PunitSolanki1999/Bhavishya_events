from django.urls import path
from .views import birthday_party,decoration_file,home_view,services_view,Theme_party,decoration,decoration_show,theme_party_show,upload,admin_auth,logout,theme_party_delete,theme_party_delete_confirm,theme_party_delete_show,decoration_delete,decoration_delete_confirm,decoration_delete_show,delete,contact_us_view,admin_request_seen_view,request_info,terms_of_service,privacy_policy
 
app_name = 'events'

urlpatterns = [
    
#this are user interface pages
    #0.this are terms of service and privacy policy urls
    path('Term_Of_Services/',terms_of_service,name='terms-of-services'),
    path('Privacy_Policy/',privacy_policy,name='privacy-policy'),

    #1.this are normal pages of html
    path('',home_view,name='home'),
    path('services/',services_view,name='services'),
    path('theme_party/',Theme_party,name='theme-party'),
    path('decoration/',decoration,name='decoration'),
    path('contact_us/',contact_us_view,name='contact-us'),

    #2.this are for showing images to user
    path('decoration_show/',decoration_show,name='decoration-show'),
    path('theme_party_show/',theme_party_show,name='theme-party-show'),

#admin interface
    #this are to upload images in database
    path('upload/',upload,name='upload'),
    path('theme_party_update/',birthday_party,name='theme-party-update'),
    path('decoration_update/',decoration_file,name='decoration-update'),

    #this are to delete images from database
    path('delete/',delete,name='delete'),
    path('theme_party_delete/',theme_party_delete,name="theme-party-delete"),
    path('theme_party_delete_show/',theme_party_delete_show,name="theme-party-delete-show"),
    path('theme_party_delete_confirm/<int:pk>/',theme_party_delete_confirm,name="theme-party-delete-confirm"),
    path('decoration_delete/',decoration_delete,name="decoration-delete"),
    path('decoration_delete_show/',decoration_delete_show,name="decoration-delete-show"),
    path('decoration_delete_confirm/<int:pk>/',decoration_delete_confirm,name="decoration-delete-confirm"),
    
    #this is for admin login,logout and user request message pages
    path('Admin_auth/',admin_auth,name='admin-auth'),
    path('admin_request_seen/',admin_request_seen_view,name='admin-request-seen'),
    path('request_info/<int:pk>/',request_info,name='request-info'),
    path('logout/',logout,name='logout'),
    
]