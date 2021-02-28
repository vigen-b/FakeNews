from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import News, Category

items_per_page = 10


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "main_category_link",
        "created_at",
    )
    search_fields = ("main_category__name__contains", "created_at")
    fields = (("title", "main_category"), "text", "owner")
    list_per_page = items_per_page

    def main_category_link(self, obj):
        url = (
            reverse("admin:news_category_changelist") + f"{obj.main_category.id}/change"
        )
        return format_html('<a href="{}">{}</a>', url, obj.main_category.name)

    main_category_link.short_description = "Main Category"

admin.site.register(Category)
