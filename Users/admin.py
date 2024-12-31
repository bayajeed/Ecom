from django.contrib import admin
from .models import CustomUser
#from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth.models import User

# Register your models here.
admin.site.register(CustomUser) # Registering CustomUser model in admin panel, (na add korle admin panel e dekha jabe na)
#admin.site.register(User, UserAdmin) # Registering the default User model