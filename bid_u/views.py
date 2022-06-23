from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Message, Donation, Contact
from django.http import HttpResponseRedirect


def home_view(request):
  if request.method == "POST":
    subscriptions = Message()

    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    if name == '':
      messages.error(request, "Name can't be empty")
    if email == '':
      messages.error(request, "Email can't be empty")
    if message == '':
      messages.error(request, "Message can't be empty")

    subscriptions.save()
    messages.success(request, "Your Message was successfully sent")
  else:
    subscriptions = Message()
  return render(request, 'index.html')


def gallery_view(request):
  return render(request, 'gallery.html')


def contact_view(request):
  if request.method == "POST":
    contact = Contact()

    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    if name == '':
      messages.error(request, "Name can't be empty")
    if email == '':
      messages.error(request, "Email can't be empty")
    if message == '':
      messages.error(request, "Message can't be empty")

    contact.save()
    messages.success(request, "Your Message was successfully sent")
  else:
    contact = Contact()
  return render(request, 'contact.html')


def about_view(request):
  return render(request, 'about.html')

def causes_view(request):
  return render(request, 'causes.html')


def donate_view(request):
  '''
  if request.method == "POST":
    donate = Donation()

    firstName = request.POST.get('firstName')
    lastName = request.POST.get('lastName')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    address = request.POST.get('address')
    note = request.POST.get('note')

    if firstName == '' and lastName =='':
      messages.error(request, "first and last name can't be empty")
    if email == '':
      messages.error(request, "Email can't be empty")
    if phone == '':
      messages.error(request, "Phone can't be empty")
    if address == '':
      messages.error(request, "Address can't be empty")
    if note == '':
      messages.error(request, "Note can't be empty")

    donate.save()
    messages.success(request, "Your Message was successfully sent")
  else:
    subscriptions = Contact()
  return render(request, 'donate.html')
      '''
  return HttpResponseRedirect('https://paystack.com/pay/bid-u-donations')


