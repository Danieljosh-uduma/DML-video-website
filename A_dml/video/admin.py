from django.contrib import admin
from .models import Video
from embed_video.admin import AdminVideoMixin

class AdminVideo(AdminVideoMixin, admin.ModelAdmin):
    pass

#Register your models here.
admin.site.register(Video, AdminVideo)