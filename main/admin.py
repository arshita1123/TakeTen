from django.contrib import admin
from main.models import Contact
from main.models import Song, Watchlater, History, Channel



admin.site.register(Song)
admin.site.register(Watchlater)
admin.site.register(History)
admin.site.register(Channel)
admin.site.register(Contact)
# Register your models here.
