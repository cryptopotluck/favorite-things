from django.contrib import admin

# Register your models here.
from .models import Users



class Profiles(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name' )
    list_display_links = ('id', 'user', )
    search_fields = ('user', 'id')
    list_per_page = 25



admin.site.register(Users, Profiles)