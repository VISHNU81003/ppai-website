from django.shortcuts import render
from .models import SiteSetting, CarouselSlide

def home(request):
    site_settings = SiteSetting.objects.first()
    slides = CarouselSlide.objects.filter(is_active=True)
    
    context = {
        'site_settings': site_settings,
        'slides': slides,
    }
    return render(request, 'pages/home.html', context)
