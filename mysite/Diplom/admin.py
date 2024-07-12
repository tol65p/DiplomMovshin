from django.contrib import admin

# Register your models here.
from . models import Users, Runners, Events, CheckPoints, AgeCategory, Protokols, ResultDetail
admin.site.register(Users)
admin.site.register(Runners)
admin.site.register(Events)
admin.site.register(CheckPoints)
admin.site.register(AgeCategory)
admin.site.register(Protokols)
admin.site.register(ResultDetail)
