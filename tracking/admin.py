from django.contrib import admin
from .models import PriorityTracking, PriorityWithSigTracking, ExpressPriorityTracking, ExpressWithSigPriorityTracking


class FileAdmin(admin.ModelAdmin):
    list_display = ["priority", "user"]

class FileAdmin1(admin.ModelAdmin):
    list_display = ["priority_with_sig", "user"]

class FileAdmin2(admin.ModelAdmin):
    list_display = ["express_priority", "user"]

class FileAdmin3(admin.ModelAdmin):
    list_display = ["express_priority_with_sig", "user"]
    

# Register your models here.
admin.site.register(PriorityTracking, FileAdmin)
admin.site.register(PriorityWithSigTracking, FileAdmin1)
admin.site.register(ExpressPriorityTracking, FileAdmin2)
admin.site.register(ExpressWithSigPriorityTracking, FileAdmin3)
