from django.contrib import admin
from .models import Message, Donation, Contact

admin.site.register(Message)
admin.site.register(Donation)
admin.site.register(Contact)
