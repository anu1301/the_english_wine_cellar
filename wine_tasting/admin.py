from django.contrib import admin
from .models import Experiences


class ExperiencesAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'price',
        'image',
        'pk',
    )

    ordering = ('name',)


admin.site.register(Experiences, ExperiencesAdmin)
