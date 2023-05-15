from django.contrib import admin
from .models import NewsLetterSub


class NewsLetterSubAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'date',)

    search_fields = ('email', 'date',)


admin.site.register(NewsLetterSub, NewsLetterSubAdmin)
