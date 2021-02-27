from django.db import models


class News(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        "auth.User", related_name="news", on_delete=models.CASCADE, null=False
    )
    text = models.TextField(blank=False, null=False)
    main_category = models.OneToOneField(
        "Category", on_delete=models.CASCADE, related_name="main_news", null=False
    )

    class Meta:
        ordering = ["created_at"]


class Category(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, unique=True)
    news = models.ManyToManyField(News, blank=True)
