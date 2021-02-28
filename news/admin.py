from django.contrib import admin

from .models import News, Category


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass


# admin.site.register(News)


admin.site.register(Category)
