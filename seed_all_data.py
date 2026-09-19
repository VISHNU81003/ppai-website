import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from pages.models import (
    SiteSetting, CarouselSlide, ExecutiveMember, PastBearer,
    EditorialBoardMember, PublicationBook, ConferenceEvent,
    SocietyAward, JournalVolume, JournalArticle
)

print("Starting PPAI Full Data Seeding...")

# 1. SiteSetting
site, _ = SiteSetting.objects.get_or_create(
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

# 2. Executive Members
executive_members_data = [
    ('Dr. S. N. Sushil', 'President', 'Director, ICAR-NBAIR, Bengaluru', 1),
    ('Dr. K. T. Rao', 'Vice President', 'ANGRAU, Guntur', 2),
    ('Dr. Subhash Chander', 'Vice President', 'Director, ICAR-NCIPM, New Delhi', 3),
    ('Dr. G. Anitha', 'General Secretary', 'Professor, PJTSAU, Rajendranagar, Hyderabad', 4),
    ('Dr. B. Sarath Babu', 'Joint Secretary', 'Head, ICAR-NBPGR Regional Station, Hyderabad', 5),
    ('Dr. C. Gopalakrishnan', 'Joint Secretary', 'Principal Scientist, ICAR-IIHR, Bengaluru', 6),
    ('Dr. M. Nagesh', 'Treasurer', 'Principal Scientist, ICAR-NBPGR RS, Hyderabad', 7),
    ('Dr. C. Chattopadhyay', 'Chief Editor', 'Former Director, ICAR-NCIPM, New Delhi', 8),
    ('Dr. S. J. Rahman', 'Council Member', 'Former Head, Dept. of Entomology, PJTSAU', 9),
    ('Dr. V. K. Baranwal', 'Council Member', 'Former Head, Plant Pathology, ICAR-IARI', 10),
    ('Dr. R. K. Sharma', 'Council Member', 'Principal Scientist, ICAR-IARI, New Delhi', 11),
    ('Dr. T. V. K. Singh', 'Council Member', 'Former Dean, PJTSAU, Hyderabad', 12),
    ('Dr. K. S. Varaprasad', 'Council Member', 'Former Director, ICAR-IIOR, Hyderabad', 13),
    ('Dr. Gururaj Katti', 'Council Member', 'Former Head, Entomology, ICAR-IIRR', 14),
    ('Dr. B. V. Patil', 'Council Member', 'Former Vice Chancellor, UAS Raichur', 15),
]

for name, desig, aff, order in executive_members_data:
    ExecutiveMember.objects.update_or_create(
        name=name,
        defaults={'designation': desig, 'affiliation': aff, 'order': order}
    )

# 3. Past Office Bearers (Legends)
past_bearers_data = [
    ('president', 'Dr. S. N. Banerjee', '1972 – 1976', 1),
    ('president', 'Dr. K. D. Paharia', '1977 – 1980', 2),
    ('president', 'Dr. N. C. Joshi', '1981 – 1985', 3),
    ('president', 'Dr. V. Ragunathan', '1986 – 1992', 4),
    ('president', 'Dr. D. B. Reddy', '1993 – 1998', 5),
    ('president', 'Dr. K. S. Varaprasad', '1999 – 2008', 6),
    ('president', 'Dr. S. N. Sushil', '2009 – Present', 7),
    ('secretary', 'Dr. K. D. Paharia', '1972 – 1978', 1),
    ('secretary', 'Dr. C. S. Sengupta', '1979 – 1986', 2),
    ('secretary', 'Dr. B. Sarath Babu', '1987 – 2012', 3),
    ('secretary', 'Dr. G. Anitha', '2013 – Present', 4),
    ('treasurer', 'Dr. M. Nagesh', '2010 – Present', 1),
    ('editor', 'Dr. C. Chattopadhyay', '2012 – Present', 1),
]

for role, name, tenure, order in past_bearers_data:
    PastBearer.objects.update_or_create(
        name=name, role=role,
        defaults={'tenure': tenure, 'order': order}
    )

# 4. Editorial Board Members
editorial_data = [
    ('chief_editor', 'Dr. C. Chattopadhyay', 'Former Director, ICAR-NCIPM, New Delhi', 1),
    ('assoc_editor', 'Dr. S. N. Sushil', 'Director, ICAR-NBAIR, Bengaluru', 2),
    ('assoc_editor', 'Dr. M. Nagesh', 'Principal Scientist, ICAR-NBPGR RS, Hyderabad', 3),
    ('member', 'Dr. G. Anitha', 'Professor, PJTSAU, Hyderabad', 4),
    ('member', 'Dr. B. Sarath Babu', 'Head, ICAR-NBPGR RS, Hyderabad', 5),
    ('intl_member', 'Prof. John A. Pickett', 'Cardiff University, UK', 6),
]

for role, name, inst, order in editorial_data:
    EditorialBoardMember.objects.update_or_create(
        name=name,
        defaults={'role': role, 'institution': inst, 'order': order}
    )

# 5. Publication Books
books_data = [
    (2016, 'Plant Protection in India: Challenges and Next Generation Strategies (ISBN: 978-81-925727-0-4)'),
    (2002, 'Plant Protection in New Millennium (Volumes 1 & 2)'),
    (1992, 'Integrated Pest Management in Indian Agriculture'),
]

for yr, title in books_data:
    PublicationBook.objects.update_or_create(
        title=title,
        defaults={'year': yr}
    )

# 6. Conference Events
conferences_data = [
    (2023, 'Golden Jubilee International Conference on Plant Protection (ICPP 2023), Hyderabad'),
    (2018, 'National Symposium on Plant Protection in Changing Climate Scenarios, ICAR-NBPGR RS'),
    (2012, 'National Seminar on Eco-Friendly Approaches in IPM for Sustainable Agriculture, ANGRAU'),
    (1986, 'First National Seminar on Plant Protection in India, CPPTI Hyderabad'),
]

for yr, title in conferences_data:
    ConferenceEvent.objects.update_or_create(
        event_title=title,
        defaults={'year': yr}
    )

# 7. Society Awards
awards_data = [
    ('Fellow of PPAI (FPPAI)', 'Conferred upon eminent scientists with >15 years of exceptional research contributions in plant protection.'),
    ('Dr. S. N. Banerjee Outstanding Scientist Award', 'Recognizes senior scientists for lifetime achievements in crop protection & IPM development.'),
    ('Dr. D. B. Reddy Young Scientist Award', 'Awarded biennially to young researchers below 35 years for outstanding original research.'),
    ('Best Ph.D Thesis Award in Plant Protection', 'Presented to Ph.D scholars from Indian Agricultural Universities/ICAR Institutes.'),
    ('Best Oral & Poster Presentation Awards', 'Presented to student and scientist delegates presenting outstanding research papers at PPAI Symposia.'),
]

for name, desc in awards_data:
    SocietyAward.objects.update_or_create(
        name=name,
        defaults={'conferred_for': desc}
    )

# 8. Journal Volumes (Vol. 42 to Vol. 54)
for vol_num in range(42, 55):
    yr = 2014 + (vol_num - 42)
    JournalVolume.objects.get_or_create(
        volume_number=vol_num,
        defaults={'year': yr, 'issues_available': 'Issues 1, 2, 3, 4'}
    )

# 9. Current Issue Sample Articles (Vol. 54, 2026, Issue 1 & Issue 2)
pdf_dir = os.path.join('media', 'journals', 'pdf')
os.makedirs(pdf_dir, exist_ok=True)

sample_pdf_path = os.path.join(pdf_dir, 'sample_article.pdf')
if not os.path.exists(sample_pdf_path):
    with open(sample_pdf_path, 'wb') as f:
        f.write(b'%PDF-1.4\n1 0 obj<</Type/Catalog/Pages 2 0 R>>endobj 2 0 obj<</Type/Pages/Count 1/Kids[3 0 R]>>endobj 3 0 obj<</Type/Page/MediaBox[0 0 612 792]/Parent 2 0 R/Resources<<>>>>endobj\nxref\n0 4\n0000000000 65535 f\n0000000009 00000 n\n0000000052 00000 n\n0000000101 00000 n\ntrailer<</Size 4/Root 1 0 R>>\nstartxref\n178\n%%EOF\n')

articles_data = [
    (54, 1, 2026, 'Efficacy of Entomopathogenic Fungi Against Fall Armyworm (Spodoptera frugiperda) in Maize', 'R. K. Sharma, S. N. Sushil, & G. Anitha', 'Field evaluations of Metarhizium anisopliae and Beauveria bassiana formulations for fall armyworm management in Telangana.'),
    (54, 1, 2026, 'Morphological and Molecular Identification of Root-Knot Nematodes (Meloidogyne spp.) Infesting Protected Cultivation', 'M. Nagesh & B. Sarath Babu', 'Assessment of species diversity and host resistance in greenhouse tomato cultivars.'),
    (54, 2, 2026, 'Integrated Management of Bacterial Leaf Blight in Rice Using Bio-Agents and Resistance Inducers', 'C. Chattopadhyay & K. T. Rao', 'Evaluation of Pseudomonas fluorescens and salicylic acid elicitors under high disease pressure conditions.'),
    (54, 2, 2026, 'Chemical Ecology and Semiochemical Response of Spodoptera litura in Cotton Ecosystems', 'Subhash Chander & C. Gopalakrishnan', 'Flight response and sex pheromone trap density optimization for monitoring field populations.'),
]

for vol_num, issue, yr, title, authors, abstract in articles_data:
    art, created = JournalArticle.objects.get_or_create(
        volume=vol_num, issue=issue, title=title,
        defaults={
            'year': yr,
            'authors': authors,
            'abstract': abstract,
            'pdf_file': 'journals/pdf/sample_article.pdf'
        }
    )
    if not art.pdf_file:
        art.pdf_file = 'journals/pdf/sample_article.pdf'
        art.save()

print("ALL PPAI Data & Sample PDFs seeded successfully!")
