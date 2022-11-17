from sqlite3 import Date
from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import user_query,court,booking
import time
from datetime import date, datetime

# Create your views here.
def index(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        court_id = request.POST.get("court_id")
        hour = request.POST.get("time")
        Booking = booking(user_id=user_id,court_id=court_id,hour=hour,date=datetime.today())
        Booking.save()
        # print(booking)
    return render(request , 'index.html')
    # return HttpResponse("this is homepage")

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # validation
        value = {
            'name' :name,
            'username' :username,
            'email' :email ,
        }
        agree = request.POST.get('agree-term','off')
        error_message = ""
        if not name:
            error_message = "Name required!!"
        elif len(name) < 3:
            error_message = "Name should be atleast of 3 characters!!"
        elif not username:
            error_message = "Username can't be blank!!"
        elif len(username) < 3:
            error_message = "Username should be atleast of 3 characters!!" 
        elif not email:
            error_message = "Email Required !!" 
        elif email[0]=='@':
            error_message = "invalid email address !!"
        elif not pass1:
            error_message = "Password Required !!"
        elif len(pass1) < 6:
            error_message = "Password can't be smaller than 6 characters!!"
        elif not pass2:
            error_message = "Confirm Password can't be blank!!"      
        

        if not error_message:
            if pass1==pass2:
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username already in use!')
                    return redirect('/register/')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Your email id already exists!')
                    return redirect('/register/')
                else:        
                    # if agree == "on":
                    user = User.objects.create_user(first_name=name,username=username, email=email,password = pass1)
                    user.save();
                    return redirect('/login/')
                #     else:
                #         messages.info(request,"Process can't be completed without agreeing to TERMS and CONDITIONS")
                #         return redirect('/register/') 
                
            else:
                messages.info(request,"Password doesn't match") 
                return redirect('/register/')    
        else:
            data ={
                'error' : error_message,
                'values' : value
            }   
            return render(request,"register.html",data)      
           

    else:
        return render(request,"register.html") 
    #return HttpResponse("register")

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if not username:
            messages.info(request,"To log in, enter your username!")
            return redirect("/login/")
        elif not password:
            messages.info(request,"To log in, enter your password!")
            return redirect("/login/")
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"Invalid Credentials!")
            return redirect('/login/')    
    else:    
        return render(request,"login.html")
    

def logout(request):
    auth.logout(request)
    return redirect('/')

def aboutus(request):
    return HttpResponse("aboutus")

def booking_page(request):
    all_court_name = court.objects.all()
    demo = {
        'court_list' : all_court_name,
    }
    return render(request,"bookcourt.html",demo)
    # return render(request,"bookcourt.html")

def court_description_page(request, court_id):
    c_id = court_id
    court_detail = court.objects.filter(pk=court_id)
    if court_detail:
        today = date.today()
        booked_detail = booking.objects.filter(date=today).filter(court_id=c_id)
        # booked_detail = 
        t = time.localtime() 
        h = t.tm_hour 
        arr = []
        for hr in range(h,24):
            val = 1
            for details in booked_detail:
                if details.hour == hr:
                    val *= 0
            if val != 0:
                arr.append(hr)
        demo = {
                    'court_list' : court_detail,
                    'time_available' : arr
                }
        return render(request,"court_desc.html",demo)
        # return HttpResponse(response)

def booking_description_page(request,user_id):
    all_booking_name = booking.objects.filter(user_id=user_id)
    demo = {
        'booking_list' : all_booking_name,
    }
    return render(request,"booklist.html",demo)


def status_page(request):
    all_court_name = court.objects.all()
    demo = {
        'court_list' : all_court_name,
    }
    return render(request,"check_status.html",demo)
    # return render(request,"bookcourt.html")


def court_status_page(request, court_id):
    c_id = court_id
    court_detail = court.objects.filter(pk=court_id)
    if court_detail:
        today = date.today()
        booked_detail = booking.objects.filter(date=today).filter(court_id=c_id)
        # booked_detail = 
        t = time.localtime() 
        h = t.tm_hour 
        arr = []
        for hr in range(h,24):
            val = 1
            for details in booked_detail:
                if details.hour == hr:
                    val *= 0
            if val != 0:
                arr.append(hr)
        demo = {
                    'court_list' : court_detail,
                    'time_available' : arr
                }
        return render(request,"court_status.html",demo)
        # return HttpResponse(response)
