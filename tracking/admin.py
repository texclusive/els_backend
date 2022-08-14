from django.contrib import admin
from .models import PriorityTracking, PriorityWithSigTracking, ExpressPriorityTracking, ExpressWithSigPriorityTracking, LabelData, LabelList


class FileAdmin(admin.ModelAdmin):
    list_display = ["priority", "user"]

class FileAdmin1(admin.ModelAdmin):
    list_display = ["priority_with_sig", "user"]

class FileAdmin2(admin.ModelAdmin):
    list_display = ["express_priority", "user"]

class FileAdmin3(admin.ModelAdmin):
    list_display = ["express_priority_with_sig", "user"]

class FileAdmin4(admin.ModelAdmin):
    list_display = ["senderData"]

class FileAdmin5(admin.ModelAdmin):
    list_display = ["mylist"]

# Register your models here.
admin.site.register(PriorityTracking, FileAdmin)
admin.site.register(PriorityWithSigTracking, FileAdmin1)
admin.site.register(ExpressPriorityTracking, FileAdmin2)
admin.site.register(ExpressWithSigPriorityTracking, FileAdmin3)
admin.site.register(LabelData, FileAdmin4)
admin.site.register(LabelList, FileAdmin5)