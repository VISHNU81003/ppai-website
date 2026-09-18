import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from pages.models import CarouselSlide, SiteSetting

site, created = SiteSetting.objects.get_or_create(
    id=1,
    defaults={
        'site_title': 'Plant Protection Association of India',
        'registration_info': '(Regn. No. S399 of 1949-50 under the Societies Registration Act XXI of 1860)',
        'logo': 'logo/ppai_logo.png'
    }
)
if not site.logo:
    site.logo = 'logo/ppai_logo.png'
    site.save()

slides_data = [
    (0, 'carousel/journal_cover.png', 'Indian Journal of Plant Protection Vol 54 No 1 Cover'),
    (1, 'carousel/slide1.jpg', 'Moth on Leaf'),
    (2, 'carousel/slide2.jpg', 'Ladybug on Plant'),
    (3, 'carousel/slide3.jpg', 'Plant Disease Spot'),
    (4, 'carousel/slide4.jpg', 'Hands Holding Seedling'),
]

for order, img, title in slides_data:
    slide, _ = CarouselSlide.objects.get_or_create(
        order=order,
        defaults={'image': img, 'title': title, 'is_active': True}
    )
    if slide.image != img:
        slide.image = img
        slide.title = title
        slide.save()

print("Default carousel slides including Journal Cover seeded successfully!")
