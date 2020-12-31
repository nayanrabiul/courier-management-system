from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Officer)
admin.site.register(Disp)
admin.site.register(Product)

