from django.contrib import admin
from .models import ChurchActivityModel,SecondChurchActivityModel
from .models import Ministries
from .models import Pastors
from .models import UpcomingEvent


class AdminChurchActivity (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title','content','author','img','slug']
admin.site.register(ChurchActivityModel,AdminChurchActivity)

class AdminSecondChurchActivityModel (admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title','content','author','img','slug']
admin.site.register(SecondChurchActivityModel,AdminSecondChurchActivityModel)

class AdminMinistries(admin.ModelAdmin):
    list_display = []
admin.site.register(Ministries,AdminMinistries)

class AdminPastors (admin.ModelAdmin):
    list_display = []
admin.site.register(Pastors, AdminPastors)

class AdminUpcomingEvent (admin.ModelAdmin):
    list_display = []
admin.site.register(UpcomingEvent, AdminUpcomingEvent)