from django.contrib import admin
from contact.models import Contact

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display=('User_Name','Password','Confirm_Password','Email','Phone','About_Yourself')

admin.site.register(Contact, ContactAdmin)
