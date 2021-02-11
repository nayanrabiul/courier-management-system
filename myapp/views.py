from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import *
from .models import *
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import user_passes_test

import datetime
from django.db.models import Sum
from django.db import connection, transaction
import re


def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(request.user, request.POST)
            if form.is_valid():
                user = form.save()
                update_session_auth_hash(request, user)
                messages.success(
                    request, 'Your password was successfully updated!')
                return redirect('/')
            else:
                messages.error(request, 'Please correct the error below.')
        else:
            form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {
            'form': form
        })
    else:
        return HttpResponsesddf("Please Log in")


def user_is_not_logged_in(user):
    return not user.is_authenticated()


def home(request):
    if request.user.is_authenticated:
        if(request.user.is_admin):
            return redirect('admin_user')
        elif(request.user.is_officer):
            return redirect('officer')
        elif(request.user.is_disp):
            return redirect('disp')
    context = {}
    return render(request, 'home.html', context)


def admin_user(request):
    # role
    if request.user.is_authenticated:
        if(request.user.is_admin):
            users = User.objects.all()
            product = Product.objects.filter()
            context = {'userss': users}
            return render(request, 'admin_user.html',  {'userss': users, 'product': product})
        else:
            return HttpResponse('error <br> You are not admin')
    else:
        return HttpResponse(' you are not logged in <br> please log in ')


def officer(request):

    if request.user.is_authenticated:
        if(request.user.is_admin):
            return redirect('admin_user')
        elif(request.user.is_disp):
            return redirect('disp')
        else:
            product = Product.objects.filter(
                reciver_location=request.user.location, product_is_arrived=True, is_retuned=False)
            need_to_return = Product.objects.filter(
                sender_location=request.user.location, retuned=True, is_retuned=True)
            product_that_returned = Product.objects.filter(
                reciver_location=request.user.location, product_is_arrived=True, is_retuned=True)
            context = {'d_product': product, 'need_to_return': need_to_return,
                       'product_that_returned': product_that_returned}
            return render(request, 'officer.html', context)
    else:
        return HttpResponse('you are not logged in.please log in ')


def branch_product(request):
    d_product = Product.objects.filter(
        product_officer=request.user.username, sender_location=request.user.location)
    print(request.user.username)
    context = {'product': d_product}
    return render(request, 'branch_product.html', context)


def disp(request):
    # rol
    if request.user.is_authenticated:
        if(request.user.is_admin):
            return redirect('admin_user')
        elif(request.user.is_officer):
            return redirect('officer')
        else:
            product = Product.objects.filter(
                reciver_location=request.user.location)

            product_that_returned = Product.objects.filter(
                sender_location=request.user.location,  is_retuned=True)

            context = {'product': product,
                       'product_that_returned': product_that_returned}
            return render(request, 'disp.html', context)

    else:
        return HttpResponse('you are not logged in.please log in ')


def registerPage(request):

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        else:
            print(form.errors)

    if request.user.is_authenticated:
        if(request.user.is_admin):
            form = CreateUserForm()
            context = {'form': form}
            return render(request, 'register.html', context)
        if(request.user.is_officer):
            return HttpResponse('error <br> You are not admin')
        elif(request.user.is_disp):
            return HttpResponse('error <br> You are not admin')
    else:
        return HttpResponse('you are not logged in.please log in ')

    form = CreateUserForm()
    context = {'form': form}
    return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        if(request.user.is_admin):
            return redirect('admin_user')
        elif(request.user.is_officer):
            return redirect('officer')
        elif(request.user.is_disp):
            return redirect('disp')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if(user.is_admin):
                return redirect('admin_user')
            elif(user.is_officer):
                return redirect('officer')
            elif(user.is_disp):
                return redirect('disp')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')


def update_user(request, pk):
    user = User.objects.get(username=pk)
    form = UserUpdateForm(instance=user)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'user_update_form.html', context)


def delete_user(request, pk):
    user = User.objects.get(username=pk)
    if request.method == "POST":
        user = User.objects.get(username=pk)
        user.delete()
        return redirect('/')
    context = {'item': user}
    return render(request, 'delete.html', context)


def view_product(request, pk):
    product = Product.objects.filter(product_id=pk)
    print(product)
    context = {'product': product}
    return render(request, 'product_view_form.html', context)


def view_products(request):
    product = Product.objects.filter()
    print(product)
    context = {'product': product}
    return render(request, 'product_view_forms.html', context)


def update_product(request, pk):
    product = Product.objects.get(product_id=pk)
    form = ProductCreationForm(instance=product)
    if request.method == 'POST':
        form = ProductCreationForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'product_update_form.html', context)


def product_registration(request):
    if request.method == 'POST':
        form = ProductCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        else:
            print(form.errors)

    form = ProductCreationForm()
    context = {'form': form}
    return render(request, 'product_creation_form.html', context)


def inventory(request):
    if request.user.is_authenticated:
        if(request.user.is_admin):
            if request.method == 'POST':
                if request.POST.get('date') is not None:
                    date = request.POST.get('date')
                    date = re.split('-', date)

                    paid = Product.objects.filter(
                        product_is_paid=True, product_date=datetime.date(int(date[0]), int(date[1]), int(date[2]))).aggregate(Sum('delivery_price'))
                    due = Product.objects.filter(
                        product_is_paid=False, product_date=datetime.date(int(date[0]), int(date[1]), int(date[2]))).aggregate(Sum('delivery_price'))

                    data = Product.objects.filter(
                        product_date=datetime.date(int(date[0]), int(date[1]), int(date[2])))
                    context = {'data': data, 'paid': list(
                        paid.values()), 'due': list(due.values())}
                    return render(request, 'inventory.html', context)
                else:
                    date1 = request.POST.get('date1')
                    date2 = request.POST.get('date2')
                    paid = Product.objects.filter(
                        product_is_paid=True, product_date__range=[date1, date2]).aggregate(Sum('delivery_price'))
                    due = Product.objects.filter(
                        product_is_paid=False, product_date__range=[date1, date2]).aggregate(Sum('delivery_price'))

                    data = Product.objects.filter(
                        product_date__range=[date1, date2])
                    context = {'data': data, 'paid': list(
                        paid.values()), 'due': list(due.values())}
                    return render(request, 'inventory.html', context)

            paid = Product.objects.filter(
                product_is_paid=True).aggregate(Sum('delivery_price'))
            due = Product.objects.filter(
                product_is_paid=False).aggregate(Sum('delivery_price'))

            data = Product.objects.all()
            context = {'data': data, 'paid': list(
                paid.values()), 'due': list(due.values())}
            return render(request, 'inventory.html', context)

        else:
            return HttpResponse('error <br> You are not admin')
    else:
        return HttpResponse(' you are not logged in <br> please log in ')


def paid_for_user(request, pk):
    Product.objects.filter(product_id=pk).update(product_is_paid=True)
    return redirect('officer')


def cheakout(request):
    return render(request, 'cheakout.html')


def handler404(request, exception):
    return render(request, '404.html', status=404)


def product_return(request, pk):
    Product.objects.filter(product_id=pk).update(is_retuned=True)
    return redirect('officer')


def user_update_for_disp(request, pk):

    subject = 'Your product is arraived'
    message = 'Your product is arraived.please collect your product'
    recepient = list(Product.objects.filter(product_id=pk).values(
        'reciver_email'))[0]['reciver_email']
    send_mail(subject,
              message, settings.EMAIL_HOST_USER, [recepient], fail_silently=False)

    Product.objects.filter(product_id=pk).update(product_is_arrived=True)
    return redirect('disp')


def user_update_for_disp_return(request, pk):

    subject = 'Your product is returned'
    message = 'Your product is returned.please come to our office'
    recepient = list(Product.objects.filter(product_id=pk).values(
        'sender_email'))[0]['sender_email']
    send_mail(subject,
              message, settings.EMAIL_HOST_USER, [recepient], fail_silently=False)

    Product.objects.filter(product_id=pk).update(retuned=True)
    return redirect('disp')


def sendmail(request):

    subject = 'Welcome to DataFlair'
    message = 'Hope you are enjoying your Django Tutorials'
    recepient = 'nayan.rabiul@gmail.com'
    send_mail(subject,
              message, settings.EMAIL_HOST_USER, [recepient], fail_silently=False)
    return render(request, 'mail.html')
