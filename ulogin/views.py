from django.db.models.query import RawQuerySet
from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User,auth

from .models import Customer,Issue,Catalogue

import datetime

def login(request):
    user=request.user
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user =auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('history')
        else:
            #print('yi')
            messages.info(request,'Invalid Username or Password')
            return redirect('/')
    elif user.is_authenticated:
        return redirect('history')
    else:
        return render(request,'sign_up.html')

def signup(request):
    user=request.user
    if user.is_authenticated:
        return redirect('history')
    elif request.method=='POST':
       # print("post")
        name=request.POST['username']
        n=request.POST['fname']+' '+request.POST['lname']
        age=request.POST['age']
        gender=request.POST['gender'][0]
        email=request.POST['email']
        phone_number=request.POST['phno']
        address=request.POST['home']
        password=request.POST['password']

        if User.objects.filter(username=name).exists():
            messages.info(request,'Username Taken')
            return redirect('signup')
        else:

            user=User.objects.create_user(username=name,password=password,email=email)
            user.save();
            user2=Customer.objects.create(customer_name=n,age=age,gender=gender,email_address=email,phone_number=phone_number,home_address=address)
            user2.save();
            user1 =auth.authenticate(username=name,password=password)
            auth.login(request, user1)
            #print('user created')
            return redirect('history')
    else:
        return render(request,'sign_up2.html')

def pending(request):
    user=request.user
    if user.is_authenticated:
        hit=Issue.objects.filter(customer_id=request.user.id)
        fine=0
        context={}
        for i in hit:
            if i.fine!=None:
                fine+=i.fine
        context['Fine']=fine
        hit=hit.filter(current_status=0)
        context['books']=hit
        context['now']=datetime.datetime.now()
        return render(request,'pending.html',context)
    else:
        return redirect('login')

def history(request):
    user=request.user
    if user.is_authenticated:
        hit=Issue.objects.filter(customer_id=request.user.id)
        fine=0
        for i in hit:
            if i.fine!=None:
                fine+=i.fine
        context={
            'books':hit,
            'Fine' :fine
        }

        return render(request,'index.html',context)
    else: return redirect('login')

def catalogue(request):
    user=request.user
    if user.is_authenticated:
        hit=Issue.objects.filter(customer_id=request.user.id)
        fine=0
        context={'books': Catalogue.objects.all()}
        for i in hit:
            if i.fine!=None:
                fine+=i.fine
        u=Customer.objects.filter(customer_id=request.user.id)
        userage=0
        for i in u:
            userage=i.age
        context['userage']=userage
        context['Fine']=fine
        if request.method=="POST":
            bookname=request.POST['bookname']
            books=Catalogue.objects.filter(book_name=bookname)
            context['books']=books
            
            return render(request,'catalogue.html',context)
        else:
            return render(request,'catalogue.html',context)
    else:
        return redirect('login')

def issue(request,book_id):
    user=request.user
    if user.is_authenticated:
        bookid=book_id
        staff=1
        i=Issue.objects.create(book_id=bookid,customer_id=request.user.id,staff_id=staff)
        i.save();
        return redirect('history')
    else:
        return redirect('login')

def about_us(request):
    user=request.user
    if user.is_authenticated:
        hit=Issue.objects.filter(customer_id=request.user.id)
        fine=0
        for i in hit:
            if i.fine!=None:
                fine+=i.fine
        return render(request,'about_us.html',{'Fine':fine})
    else:
        return redirect('login')

def logout(request):
    auth.logout(request)
    return redirect('/')