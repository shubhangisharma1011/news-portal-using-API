from django.contrib import admin
from .models import CustomUser
from .models import User_Model_Email_Verification
# Register your models here.



@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','email', 'first_name', 'last_name', 'is_staff', 'phone', 'address', 'file',]


admin.site.register(User_Model_Email_Verification)