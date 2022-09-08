from django.contrib import admin
from .models import Mailme

@admin.register(Mailme)
class MailmeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'tel', 'email')
    search_fields = ['tel',]