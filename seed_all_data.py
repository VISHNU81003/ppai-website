import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from pages.models import (
    SiteSetting, CarouselSlide, ExecutiveMember, PastBearer,
    EditorialBoardMember, PublicationBook, ConferenceEvent,
    SocietyAward, JournalVolume, JournalArticle
)

print("Seeding full dataset from official document...")

# Clear existing ExecutiveMember and PastBearer to ensure clean sync with 8-page document
ExecutiveMember.objects.all().delete()
PastBearer.objects.all().delete()

# 1. SiteSetting
site, _ = SiteSetting.objects.get_or_create(
    id=1,
    defaults={
        'site_title': 'Plant Protection Association of India',
        'registration_info': '(Regn. No. S399 of 1949-50 under the Societies Registration Act XXI of 1860)',
        'logo': 'logo/ppai_logo.png'
    }
)

# 2. Executive Council (Page 2 of document)
executive_members_data = [
    ('Dr. B. Sarath Babu', 'President', 'Principal Scientist & Former Head, ICAR-NBPGR RS, Hyderabad', 'male', 'Leads the governing body of PPAI.', 1),
    ('Dr. Celia Chalam', 'Vice-President', 'Principal Scientist (Plant Pathology), ICAR-NBPGR, New Delhi', 'female', 'Plant pathology and virology specialist.', 2),
    ('Dr. M. Srinivas Prasad', 'Vice-President', 'Head & Principal Scientist (Plant Pathology), ICAR-IIRR, Hyderabad', 'male', 'Rice disease management authority.', 3),
    ('Dr. R. Jagadeeshwar', 'Vice-President', 'Director of Research (Retd.), PJTSAU, Hyderabad', 'male', 'Senior extension and crop protection researcher.', 4),
    ('Dr. B. Parameswari', 'General Secretary', 'Principal Scientist (Plant Pathology), ICAR-SBI / NBPGR RS, Hyderabad', 'female', 'Manages Association affairs & membership.', 5),
    ('Dr. V. Prakasam', 'Assistant Secretary', 'Senior Scientist, ICAR-NBPGR Regional Station, Hyderabad', 'male', 'Assists General Secretary in executive duties.', 6),
    ('Dr. Bhasker Bajaru', 'Treasurer', 'Scientist (Agricultural Entomology), ICAR-NBPGR RS, Hyderabad', 'male', 'Handles accounts, receipts, and remittances.', 7),
    ('Dr. L. Saravanan', 'Chief Editor', 'Principal Scientist (Agril. Entomology), ICAR-NBPGR RS, Hyderabad', 'male', 'Oversees IJPP peer review & quarterly issues.', 8),
    ('Dr. Kavitha Gupta', 'Associate Editor', 'Principal Scientist (Entomology), ICAR-NBPGR, New Delhi', 'female', 'Quarantine and entomology reviewer.', 9),
    ('Dr. Prasanna Holajjer', 'Associate Editor', 'Senior Scientist (Nematology), ICAR-NBPGR RS, Hyderabad', 'male', 'Nematology and plant protection editor.', 10),
    ('Dr. K. Rameash', 'Councillor', 'Principal Scientist (Agril. Entomology), ICAR-CICR / Regional Stations', 'male', 'Cotton insect pest researcher.', 11),
    ('Dr. J. Stanley', 'Councillor', 'Senior Scientist (Agril. Entomology), ICAR-VPKAS, Almora', 'male', 'Hill crop pest management specialist.', 12),
    ('Dr. B. S. Gotyal', 'Councillor', 'Senior Scientist (Agril. Entomology), ICAR-CRIJAF, Barrackpore', 'male', 'Jute and fiber crop protection researcher.', 13),
    ('Dr. D. Sagar', 'Councillor', 'Senior Scientist (Entomology), ICAR-IARI, New Delhi', 'male', 'Insect physiology & IPM scientist.', 14),
    ('Dr. Alpeshkumar V. Khanpara', 'Councillor', 'Associate Research Scientist, Junagadh Agricultural University, Gujarat', 'male', 'Groundnut & pulse protection expert.', 15),
]

for name, desig, aff, gender, bio, order in executive_members_data:
    ExecutiveMember.objects.create(
        name=name, designation=desig, affiliation=aff, gender=gender, bio=bio, order=order
    )

# 3. Past Office Bearers (Pages 3 & 4 of document)
# Past Presidents
presidents = [
    ('Dr. K. K. Nirula', 'Founder President (1972 – 1978)', 'CPPTI, Hyderabad', 'male', 1),
    ('Dr. N. C. Joshi', '1979 – 1980', 'CPPTI, Hyderabad', 'male', 2),
    ('Dr. K. D. Paharia', '1981 – 1984', 'CPPTI, Hyderabad', 'male', 3),
    ('Dr. N. C. Joshi', '1985 – 1986', 'CPPTI, Hyderabad', 'male', 4),
    ('Dr. D. Bap Reddy', '1987 – 1988', 'FAO Representative', 'male', 5),
    ('Dr. S. Jayaraj', '1989 – 1990', 'TNAU, Coimbatore', 'male', 6),
    ('Dr. D. V. R. Reddy', '1991 – 1997', 'ICRISAT, Patancheru', 'male', 7),
    ('Dr. K. Krishnaiah', '1997 – 1999', 'DRR (ICAR-IIRR), Hyderabad', 'male', 8),
    ('Dr. P. S. Chandukar', '2000 – 2002', 'PPA to Govt. of India', 'male', 9),
    ('Dr. Y. L. Nene', '2003 – 2006', 'ICRISAT / Asian Agri-History Foundation', 'male', 10),
    ('Dr. K. S. R. K. Murthy', '2007 – 2009', 'ANGRAU, Hyderabad', 'male', 11),
    ('Dr. K. S. Varaprasad', '2010 – 2012', 'ICAR-NBPGR RS / IIOR', 'male', 12),
    ('Dr. B. Sarath Babu', '2018 – 2022', 'ICAR-NBPGR RS, Hyderabad', 'male', 13),
]
for name, tenure, aff, gender, order in presidents:
    PastBearer.objects.create(role='president', name=name, tenure=tenure, affiliation=aff, gender=gender, order=order)

# Past Secretaries
secretaries = [
    ('Dr. S. S. Hussaine', '1972 – 1974', 'CPPTI, Hyderabad', 'male', 1),
    ('Dr. V. Lakshminarayana', '1975 – 1976, 1979 – 1980', 'CPPTI, Hyderabad', 'male', 2),
    ('Dr. Basu Chaudhary', '1977 – 1978', 'CPPTI, Hyderabad', 'male', 3),
    ('Dr. V. Raghunathan', '1981 – 1984', 'Central Plant Protection Station', 'male', 4),
    ('Shri B. Govinda Naik', '1985 – 1986', 'CPPTI, Hyderabad', 'male', 5),
    ('Dr. B. J. Divakar', '1987 – 1997', 'Directorate of Plant Protection', 'male', 6),
    ('Dr. Renu Sharma', '1997 – 1999', 'ICAR-NBPGR RS, Hyderabad', 'female', 7),
    ('Dr. R. D. V. J. Prasada Rao', '2000 – 2006', 'ICAR-NBPGR RS, Hyderabad', 'male', 8),
    ('Dr. S. K. Chakrabarty', '2007 – 2009', 'ICAR-NBPGR RS, Hyderabad', 'male', 9),
    ('Dr. B. Sarath Babu', '2010 – 2012', 'ICAR-NBPGR RS, Hyderabad', 'male', 10),
    ('Dr. R. Jagadeeshwar', '2018 – 2020', 'PJTSAU, Hyderabad', 'male', 11),
    ('Dr. B. Parameswari', '2020 – 2022', 'ICAR-NBPGR RS, Hyderabad', 'female', 12),
]
for name, tenure, aff, gender, order in secretaries:
    PastBearer.objects.create(role='secretary', name=name, tenure=tenure, affiliation=aff, gender=gender, order=order)

# Past Treasurers
treasurers = [
    ('Shri P. K. Menon', '1972 – 1974', 'CPPTI, Hyderabad', 'male', 1),
    ('Shri S. S. Lal', '1975 – 1976', 'CPPTI, Hyderabad', 'male', 2),
    ('Shri T. Rengarajan', '1977 – 1980, 1987 – 1990', 'CPPTI, Hyderabad', 'male', 3),
    ('Dr. A. Jayaprakash', '1981 – 1984', 'CPPTI, Hyderabad', 'male', 4),
    ('Dr. B. J. Divakar', '1985 – 1986', 'CPPTI, Hyderabad', 'male', 5),
    ('Mr. D. Chatterjee', '1991 – 1993', 'CPPTI, Hyderabad', 'male', 6),
    ('Mr. C. V. Rama Rao', '1993 – 1999', 'ANGRAU, Hyderabad', 'male', 7),
    ('Dr. K. Anitha', '2000 – 2004', 'ICAR-NBPGR RS, Hyderabad', 'female', 8),
    ('Dr. S. K. Chakrabarty', '2005 – 2006, 2010 – 2012', 'ICAR-NBPGR RS, Hyderabad', 'male', 9),
    ('Dr. Kamala Venkateswaran', '2007 – 2009', 'ICAR-NBPGR RS, Hyderabad', 'female', 10),
    ('Dr. Prasanna Holajjer', '2018 – 2020', 'ICAR-NBPGR RS, Hyderabad', 'male', 11),
    ('Dr. Bhasker Bajaru', '2020 – 2022', 'ICAR-NBPGR RS, Hyderabad', 'male', 12),
]
for name, tenure, aff, gender, order in treasurers:
    PastBearer.objects.create(role='treasurer', name=name, tenure=tenure, affiliation=aff, gender=gender, order=order)

# Past Chief Editors
editors = [
    ('Shri B. K. Verma', '1972 – 1976', 'CPPTI, Hyderabad', 'male', 1),
    ('Dr. V. Lakshminarayana', '1977 – 1978', 'CPPTI, Hyderabad', 'male', 2),
    ('Dr. K. K. Nirula', '1979 – 1982', 'CPPTI, Hyderabad', 'male', 3),
    ('Dr. M. Veerabhadra Rao', '1983 – 1993', 'CPPTI / ANGRAU', 'male', 4),
    ('Dr. H. C. Sharma', '1993 – 1995', 'ICRISAT, Patancheru', 'male', 5),
    ('Dr. T. B. Gour', '1995 – 1999', 'ANGRAU, Hyderabad', 'male', 6),
    ('Dr. K. S. Varaprasad', '2000 – 2004', 'ICAR-NBPGR RS, Hyderabad', 'male', 7),
    ('Dr. B. Sarath Babu', '2005 – 2009', 'ICAR-NBPGR RS, Hyderabad', 'male', 8),
    ('Dr. Gururaj Katti', '2010 – 2012', 'DRR (ICAR-IIRR), Hyderabad', 'male', 9),
    ('Dr. G. Sridevi', '2018 – 2020', 'PJTSAU, Hyderabad', 'female', 10),
    ('Dr. L. Saravanan', '2020 – 2022', 'ICAR-NBPGR RS, Hyderabad', 'male', 11),
]
for name, tenure, aff, gender, order in editors:
    PastBearer.objects.create(role='editor', name=name, tenure=tenure, affiliation=aff, gender=gender, order=order)

print("Database synced cleanly with 8-page document OCR text!")
