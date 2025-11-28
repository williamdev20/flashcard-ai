from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify

User = get_user_model()

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(blank=False, null=False)

    class Meta:
        unique_together = [ # Um usuário não pode ter duas categorias com o mesmo nome, mas usuários diferentes sim
            ("user", "name"),
            ("user", "slug")
        ] 
        verbose_name = "Category"
        verbose_name_plural = "Categories"


    def save(self, *args, **kwargs):
        if not self.slug and self.slug is not None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return f"Category: {self.name}"
    


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(blank=False, null=False)

    def save(self, *args, **kwargs):
        if not self.slug and self.slug is not None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        unique_together = [
            ("category", "name"),
            ("category", "slug")
        ]
        verbose_name = "Subcategory"
        verbose_name_plural = "Subcategories"

    def __str__(self):
        return f"Subcategory: {self.name}"


class Deck(models.Model):
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(blank=False, null=False)

    def save(self, *args, **kwargs):
        if not self.slug and self.slug is not None:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        unique_together = [
            ("subcategory", "name"),
            ("subcategory", "slug")
        ]
        verbose_name = "Deck"
        verbose_name_plural = "Decks"

    def __str__(self):
        return f"Deck: {self.name}"