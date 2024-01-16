from django.contrib import admin
from .forms import TaskRegistration
from .models import Tasks
# Register your models here.

@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    list_display=['id','task','start_time','end_time']