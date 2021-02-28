from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import News, Category


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "main_category_link",
        "created_at",
    )

    def main_category_link(self, obj):
        url = (
            reverse("admin:news_category_changelist") + f"{obj.main_category.id}/change"
        )
        return format_html('<a href="{}">{}</a>', url, obj.main_category.name)

    main_category_link.short_description = "Main Category"


admin.site.register(Category)
