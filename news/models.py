from django.db import models


class News(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(blank=False, null=False, max_length=50)
    text = models.TextField(blank=False, null=False)
    main_category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="main_news", null=False
    )

    def __str__(self):
        return f"{self.title}, {self.main_category.name}, {self.created_at}"

    class Meta:
        ordering = ["created_at"]
        verbose_name_plural = "News"


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    news = models.ManyToManyField(News, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
