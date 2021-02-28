from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django import forms

from .models import News, Category
from tinymce.widgets import TinyMCE


class NewsForm(forms.ModelForm):
    text = forms.CharField(widget=TinyMCE(attrs={"cols": 80, "rows": 100}))

    class Meta:
        model = News
        fields = ("text",)


items_per_page = 10


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    form = NewsForm
    list_display = (
        "title",
        "main_category_link",
        "created_at",
    )
    search_fields = ("main_category__name__contains", "created_at")
    fields = (("title", "main_category"), "text")
    list_per_page = items_per_page

    def main_category_link(self, obj):
        url = (
            reverse("admin:news_category_changelist") + f"{obj.main_category.id}/change"
        )
        return format_html('<a href="{}">{}</a>', url, obj.main_category.name)

    main_category_link.short_description = "Main Category"

    class Media:
        js = [
            "/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js",
            "/static/news/js/tinymce_setup.js",
        ]


admin.site.register(Category)
