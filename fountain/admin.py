from django.contrib import admin
from .models import ChurchActivity
from .models import Ministries
from .models import Pastors
from .models import UpcomingEvent


class AdminChurchActivity (admin.ModelAdmin):
    list_display = []
admin.site.register(ChurchActivity,AdminChurchActivity)

class AdminMinistries(admin.ModelAdmin):
    list_display = []
admin.site.register(Ministries,AdminMinistries)

class AdminPastors (admin.ModelAdmin):
    list_display = []
admin.site.register(Pastors, AdminPastors)

class AdminUpcomingEvent (admin.ModelAdmin):
    list_display = []
admin.site.register(UpcomingEvent, AdminUpcomingEvent)