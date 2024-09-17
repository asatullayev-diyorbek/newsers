from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name="Nom")
    slug = models.SlugField(max_length=30, verbose_name="Slug")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Kategorilar"
        verbose_name = "Kategiriya"

    def get_newses(self):
        return News.objects.filter(category=self, is_active=True).order_by('-created_at')


class Tag(models.Model):
    title = models.CharField(max_length=30, verbose_name="Nom")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Taglar"
        verbose_name = "Tag"


class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriya")
    tags = models.ManyToManyField(Tag, verbose_name="Taglar")
    title = models.CharField(max_length=255, verbose_name="Nom")
    slug = models.SlugField(max_length=255, verbose_name="Slug")
    description = models.TextField(verbose_name="Kontent")
    image = models.ImageField(upload_to="news/images/", verbose_name="Rasm")
    views = models.PositiveIntegerField(default=0, verbose_name="Ko'rilishlar")
    shares = models.PositiveIntegerField(default=0, verbose_name="Ulashishlar")
    is_active = models.BooleanField(default=True, verbose_name="Faollik")
    is_banner = models.BooleanField(default=False, verbose_name="Bannerga joylash")
    is_weekly = models.BooleanField(default=False, verbose_name="Haftalik")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Yangiliklar"
        verbose_name = "Yangilik"

    def get_image(self):
        if self.image:
            return self.image.url
        return "https://www.testo.com/images/not-available.jpg"


class Email(models.Model):
    email = models.EmailField(verbose_name="E-mail")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqti")

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "E-maillar"
        verbose_name = "E-mail"
