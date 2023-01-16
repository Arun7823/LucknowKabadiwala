from django.contrib import admin
from contact.models import Contact
class ContactAdmin(admin.ModelAdmin):
    list_display=('username','phone','address','item')

admin.site.register(Contact,ContactAdmin)

# Register your models here.
