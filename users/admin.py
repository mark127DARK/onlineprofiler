from django.contrib import admin
from .models import User

# Register your models here.

admin.site.site_header = "Profiler Web App Admin"
admin.site.title_header = "Profiler Admin"
admin.site.index_title = "Welcome To Our Online Web App Profiler"

class UserAdmin(admin.ModelAdmin):
    list_display = [
        'user_fname',
        'user_lname',
        'user_email',
        'user_position',
    ]
    search_fields = [
        'user_fname',
        'user_lname',
        'user_email',
        'user_position',
    ]
    
admin.site.register(User, UserAdmin)


