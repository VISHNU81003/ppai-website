from django.db import models

class SiteSetting(models.Model):
    site_title = models.CharField(max_length=255, default='Plant Protection Association of India')
    registration_info = models.CharField(
        max_length=255, 
        default='(Regn. No. S399 of 1949-50 under the Societies Registration Act XXI of 1860)'
    )
    logo = models.ImageField(upload_to='logo/', blank=True, null=True)
    hero_badge = models.CharField(max_length=50, default='Since 1972')
    hero_title = models.CharField(max_length=255, default='Indian Journal of Plant Protection')
    hero_description = models.TextField(
        default='The Indian Journal of Plant Protection (IJPP) is a peer-reviewed quarterly journal published by the Plant Protection Association of India (PPAI), Hyderabad. It publishes original research, reviews, and short communications in agricultural entomology, plant pathology, nematology, weed science, and integrated pest management (IPM).'
    )
    members_count = models.CharField(max_length=50, default='1,900+')
    society_years = models.CharField(max_length=50, default='54')
    published_volumes = models.CharField(max_length=50, default='54')

    class Meta:
        verbose_name = 'Site Setting'
        verbose_name_plural = 'Site Settings'

    def __str__(self):
        return self.site_title


class CarouselSlide(models.Model):
    title = models.CharField(max_length=200, blank=True, help_text="Alt text or title for slide")
    image = models.ImageField(upload_to='carousel/')
    order = models.PositiveIntegerField(default=0, help_text="Order of display (0, 1, 2...)")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order', 'id']

    def __str__(self):
        return self.title or f"Slide {self.id}"
