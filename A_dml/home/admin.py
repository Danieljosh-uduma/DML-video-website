from django.contrib import admin
from .models import FAQs, FreeCourse, PaidCourse, UpcomingCourse, Tutors

# Register your models here.
admin.site.register(FAQs)
admin.site.register(FreeCourse)
admin.site.register(PaidCourse)
admin.site.register(UpcomingCourse)
admin.site.register(Tutors)