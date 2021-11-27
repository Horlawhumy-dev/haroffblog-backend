from django.contrib import admin
from .models import SubscribedMail

class SubscribedMailAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'date_subscribed')
    list_display_links = ('id', 'email')
    search_fields = ('email',)

admin.site.register(SubscribedMail, SubscribedMailAdmin)
