from django.contrib import admin
from .models import FAQ, FreeCourse, PaidCourse, UpcomingCourse, Tutor

# Register your models here.
admin.site.register(FAQ)
admin.site.register(FreeCourse)
admin.site.register(PaidCourse)
admin.site.register(UpcomingCourse)
admin.site.register(Tutor)