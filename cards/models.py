from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False, unique=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"Category: {self.name}"
