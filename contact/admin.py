from django.contrib import admin
from .models import ContactMessage

class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'sent_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email')

admin.site.register(ContactMessage, ContactMessageAdmin)
