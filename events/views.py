from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Birthday,Decoration,User_request#,Promotion
from .forms import Birthday_file_form,Decoration_file,User_request_form,Admin_auth_form,User_request_form#,Promotion_file
from django.contrib import sessions


from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

#This functions are for Terms of services and privacy policy
def terms_of_service(request,*args,**kwargs):
    return render(request,'events/Terms_of_service.html')

def privacy_policy(request,*args,**kwargs):
    return render(request,'events/Privacy_policy.html')

#This Function is for submitting the request to the admin for work
def contact_us_view(request,*args,**kwargs):
    form = User_request_form(request.POST or None )
    if request.method == 'POST':
        print("bye")
        if form.is_valid():
            print("hello")
            instance = form.save()
            name = instance.first_name + " " + instance.last_name
            subject = name
            message = ("Gmail address: " + instance.gmail + "\n" + "Mobile Number: " + instance.mobile_number + "\n" + "Event Details: " + instance.description)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['bhavishyaevents.hr@gmail.com',]
            send_mail( subject, message, email_from, recipient_list )
            return redirect("events:contact-us")
    context = {
        'form':form,
    }
    return render(request,'events/user_request.html',context)


#This Function is for viewing the list name of the user messages to the Admin
def admin_request_seen_view(request,*args,**kwargs):
    if request.session.has_key('username'):
        no_user = False
        try:
            user = User_request.objects.all()
            if user:
                result = reversed(list(user))
            else:
                raise Exception
        except Exception:
            no_user = True

        context = {
            'user':user,
            'result': result,
            'no_user':no_user,
        }

        return render(request,'events/admin_request_seen.html',context)
    else:
        return redirect('events:admin-auth')


#this function is for watching the user message details
def request_info(request,pk=None,*args,**kwargs):
    if request.session.has_key('username'):
        user = User_request.objects.get(pk=pk)
        user.seen = True
        user.save()
        context = {
            'user':user,
        }

        return render(request,'events/request_info.html',context)
    else:
        return redirect('events:admin-auth')


#this fuction is for uploading theme-party data to the database
def birthday_party(request,*args,**kwargs):
    if request.session.has_key('username'):
        form = Birthday_file_form(request.POST or None , request.FILES or None)
        if request.method == 'POST':
            if form.is_valid():
                instance = form.save(commit = False)
                if 'files' in request.FILES:
                    instance.party_file = request.FILES['files']
                form.save()
                return redirect('events:theme-party-update')
        context = {
            'form': form,
        }
        return render(request,'events/theme_party_form.html',context)
    else:
        return redirect('events:admin-auth')


#This function is for uploading decoration data to the database
def decoration_file(request,*args,**kwargs):
    if request.session.has_key('username'):
        form = Decoration_file(request.POST or None ,request.FILES or None)
        if request.method == 'POST':
            if form.is_valid():
                instance = form.save(commit = False)
                if 'files' in request.FILES:
                    instance.decoration_file = request.FILES['files']
                form.save()
                return redirect('events:decoration-update')
        context = {
            'form': form,
        }
        return render(request,'events/decoration_file.html',context)
    else:
        return redirect('events:admin-auth')


#this function is for seeing the home page of site
def home_view(request,*args,**kwargs):
    return render(request,'events/Home.html',{})


#this function if for seeing the admin interface first page
def upload(request,*args,**kwargs):
    if request.session.has_key('username'):
        return render(request,'events/upload.html',{})
    else:
        return redirect('events:admin-auth')


#this function is for seeing the services of event manager
def services_view(request,*args,**kwargs):

    return render(request,'events/Services.html',{})


#this function is for seeing the service of theme party
def Theme_party(request,*args,**kwargs):
    #form = Theme_party_view(request.POST or None)
    if request.session.has_key('name'):
        del request.session['name']
    if request.method == 'POST':
        data = request.POST.copy()
        if data.get('Birthday Party'):
            name = data.get('Birthday Party')
            request.session['name'] = name
            return redirect("events:theme-party-show")
        elif data.get('Cocktail Party'):
            name = data.get('Cocktail Party')
            request.session['name'] = name
            return redirect("events:theme-party-show")
        elif data.get('Kitty Party'):
            name = data.get('Kitty Party')
            request.session['name'] = name
            return redirect("events:theme-party-show")
        elif data.get('Pool Party'):
            name = data.get('Pool Party')
            request.session['name'] = name
            return redirect("events:theme-party-show")
        elif data.get('DJ Night'):
            name = data.get('DJ Night')
            request.session['name'] = name
            return redirect("events:theme-party-show")
        elif data.get('Bachlor Party'):
            name = data.get('Bachlor Party')
            request.session['name'] = name
            return redirect("events:theme-party-show")
        elif data.get('Welcome and Farewell Party'):
            name = data.get('Welcome and Farewell Party')
            request.session['name'] = name
            return redirect("events:theme-party-show")
        elif data.get('Fashion Show'):
            name = data.get('Fashion Show')
            request.session['name'] = name
            return redirect("events:theme-party-show")

    context = {
        #'form':form,
    }
    return render(request,'events/Theme_Party.html',context)


#this function is for seeing the services of decoration events
def decoration(request,*args,**kwargs):
   # form = Decoration_view(request.POST or None)
    if request.session.has_key('name'):
        del request.session['name']
    if request.method == 'POST':
        data = request.POST.copy()
        if data.get('Balloon Decoration'):
            name = data.get('Balloon Decoration')
            request.session['name'] = name
            return redirect("events:decoration-show")
        elif data.get('Flower Decoration'):
            name = data.get('Flower Decoration')
            request.session['name'] = name
            return redirect("events:decoration-show")
        elif data.get('Mall Decoration'):
            name = data.get('Mall Decoration')
            request.session['name'] = name
            return redirect("events:decoration-show")
        elif data.get('Showroom Decoration'):
            name = data.get('Showroom Decoration')
            request.session['name'] = name
            return redirect("events:decoration-show")
        elif data.get('Festival Decoration'):
            name = data.get('Festival Decoration')
            request.session['name'] = name
            return redirect("events:decoration-show")
        elif data.get('Stage Decoration'):
            name = data.get('Stage Decoration')
            request.session['name'] = name
            return redirect("events:decoration-show")

    context = {
       # 'form':form,
    }
    return render(request,'events/Decoration.html',context)


#this function is for seeing the images of decoration
def decoration_show(request,*args,**kwargs):
    if request.session.has_key('name'):
        name = request.session['name']
        print(name)
        theme = name.lower()
        user = Decoration.objects.filter(decoration__contains=theme)
        context = {
            'user': user
        } 
        return render(request,'events/decoration_show.html',context)
    else: 
        return redirect('events:decoration')


#this function is for seeing the images of theme-party
def theme_party_show(request,*args,**kwargs):
    
    if request.session.has_key('name'):
        theme = request.session['name']
        print(theme)
        theme = theme.lower()
        user = Birthday.objects.filter(party_theme__contains=theme)
        context = {
            'user': user
        }
        return render(request,'events/theme_party_show.html',context)
    else:
        return redirect('events:theme-party')


#this function is for admin authentication
def admin_auth(request,*args,**kwargs):
    if request.session.has_key('username'):
        return redirect('events:upload')
    else:
        form = Admin_auth_form( request.POST or None)
        user_not_available = False
        if request.method == 'POST':
            data = request.POST.copy()
            username = data.get('username')
            password = data.get('password')
            try:
                user = authenticate(username=username,  password=password)
                if user:
                    request.session['username'] = username
                    return redirect('events:upload')
                else: 
                    user_not_available = True
            except Exception:
                user_not_available = True

        context = {
            'user_not_available': user_not_available,
            'form': form,
        }
        return render(request,'events/Admin_auth.html',context)


#this function is for admin logout
def logout(request,*args,**kwargs):
    if request.session.has_key('username'):
        if request.method == 'POST':
            data = request.POST.copy()
            if data.get('Yes'):
                
                del request.session['username']
                return redirect('events:admin-auth')
            elif data.get('No'):
                
                return redirect('user:upload')
    return render(request,'events/logout.html')



# photo deletion functions
# 0.Page for delete files
def delete(request,*args,**kwargs):
    return render(request,'events/delete.html')
# 1.Theme Party Delete Function

def theme_party_delete_confirm(request,pk,*args,**kwargs):
    if request.session.has_key('username'):
        if request.method == 'POST':
            data = request.POST.copy()
        
            if data.get('Yes'):
                obj = Birthday.objects.get(pk=pk)
                obj.delete()
                return redirect('events:theme-party-delete-show')
            elif data.get('No'):
                return redirect('events:theme-party-delete-show')
            
        return render(request,'events/delete_confirm.html',{})
    else:
        return redirect('events:admin-auth')


def theme_party_delete_show(request,pk=None,*args,**kwargs):
    
    if request.session.has_key('username'):
        if request.session.has_key('delete_name'):
            theme = request.session['delete_name']
            print(theme)
            theme = theme.lower()
            user = Birthday.objects.filter(party_theme__contains=theme)
            context = {
                'user': user
            }
            return render(request,'events/theme_party_delete.html', context)
        else:
            return redirect('events:theme-party-delete')
    else:
        return redirect('events:admin-auth')

def theme_party_delete(request,*args,**kwargs):
    #form = Theme_party_view(request.POST or None)
    if request.session.has_key('username'):
        if request.session.has_key('delete_name'):
            del request.session['delete_name']
        if request.method == 'POST':
            data = request.POST.copy()
            if data.get('Cocktail Party'):
                name = data.get('Cocktail Party')
                request.session['delete_name'] = name
                return redirect("events:theme-party-delete-show")
            elif data.get('Kitty Party'):
                name = data.get('Kitty Party')
                request.session['delete_name'] = name
                return redirect("events:theme-party-delete-show")
            elif data.get('Pool Party'):
                name = data.get('Pool Party')
                request.session['delete_name'] = name
                return redirect("events:theme-party-delete-show")
            elif data.get('DJ Night'):
                name = data.get('DJ Night')
                request.session['delete_name'] = name
                return redirect("events:theme-party-delete-show")
            elif data.get('Bachlor Party'):
                name = data.get('Bachlor Party')
                request.session['delete_name'] = name
                return redirect("events:theme-party-delete-show")
            elif data.get('Welcome & Farewell Party'):
                name = data.get('Welcome & Farewell Party')
                request.session['delete_name'] = name
                return redirect("events:theme-party-delete-show")
            elif data.get('Fashion Show'):
                name = data.get('Fashion Show')
                request.session['delete_name'] = name
                return redirect("events:theme-party-delete-show")

        context = {
            #'form':form,
        }
        return render(request,'events/Theme_Party.html',context)
    else:
        return redirect('events:admin-auth')

# 2. Decoration Delete Function
def decoration_delete_confirm(request,pk,*args,**kwargs):
    if request.session.has_key('username'):
        if request.method == 'POST':
            data = request.POST.copy()
        
            if data.get('Yes'):
                obj = Decoration.objects.get(pk=pk)
                obj.delete()
                return redirect('events:decoration-delete-show')
            elif data.get('No'):
                return redirect('events:decoration-delete-show')
            
        return render(request,'events/delete_confirm.html',{})
    else:
        return redirect('events:admin-auth')


def decoration_delete_show(request,pk=None,*args,**kwargs):
    
    if request.session.has_key('username'):
        if request.session.has_key('delete_name'):
            theme = request.session['delete_name']
            print(theme)
            theme = theme.lower()
            user = Decoration.objects.filter(decoration__contains=theme)
            context = {
                'user': user
            }
            return render(request,'events/decoration_delete.html', context)
        else:
            return redirect('events:decortion-delete')
    else:
        return redirect('events:admin-auth')

def decoration_delete(request,*args,**kwargs):
    if request.session.has_key('username'):
        if request.session.has_key('delete_name'):
            del request.session['delete_name']
        if request.method == 'POST':
            data = request.POST.copy()
            if data.get('Balloon Decoration'):
                name = data.get('Balloon Decoration')
                request.session['delete_name'] = name
                return redirect("events:decoration-delete-show")
            elif data.get('Flower Decoration'):
                name = data.get('Flower Decoration')
                request.session['delete_name'] = name
                return redirect("events:decoration-delete-show")
            elif data.get('Mall Decoration'):
                name = data.get('Mall Decoration')
                request.session['delete_name'] = name
                return redirect("events:decoration-delete-show")
            elif data.get('Showroom Decoration'):
                name = data.get('Showroom Decoration')
                request.session['delete_name'] = name
                return redirect("events:decoration-delete-show")
            elif data.get('Festival Decoration'):
                name = data.get('Festival Decoration')
                request.session['delete_name'] = name
                return redirect("events:decoration-delete-show")
            elif data.get('Stage Decoration'):
                name = data.get('Stage Decoration')
                request.session['delete_name'] = name
                return redirect("events:decoration-delete-show")

        context = {
           # 'form':form,
        }
        return render(request,'events/Decoration.html',context)
    else:
        return redirect('events:admin-auth')

