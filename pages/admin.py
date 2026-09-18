from django.contrib import admin
from .models import SiteSetting, CarouselSlide

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    list_display = ('site_title', 'hero_title', 'members_count')

@admin.register(CarouselSlide)
class CarouselSlideAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'order', 'is_active', 'image')
    list_editable = ('order', 'is_active')
