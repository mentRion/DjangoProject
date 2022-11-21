from django.contrib import admin

from hello.models import User

class  UserAdmin(admin.ModelAdmin):
    list_display = ('id','name','email')
    search_fields = ('id','name')
    list_filter = ('college',)
    ordering = ('-college',)
    fields = ('id','email','name','college')

# Register your models here.

admin.site.register(User,UserAdmin)

