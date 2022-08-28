from django.contrib import admin

from home.models import Journey

# Register your models here.
class JourneyAdmin(admin.ModelAdmin):
    list_display = ('title',)


admin.site.register(Journey, JourneyAdmin)