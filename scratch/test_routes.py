import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

import django
django.setup()

from django.test import Client

c = Client()
routes = [
    '',
    'about/',
    'executive-council/',
    'legends/',
    'journal/current/',
    'journal/archives/',
    'journal/editorial-board/',
    'journal/guidelines/',
    'journal/books/',
    'membership/info/',
    'membership/directory/',
    'awards/',
    'awards/nomination/',
    'conferences/',
    'contact/'
]

print("--- TESTING ALL 15 LOCAL ROUTES ---")
all_ok = True
for r in routes:
    response = c.get('/' + r)
    print(f"Route: /{r:<28} -> HTTP Status {response.status_code}")
    if response.status_code != 200:
        all_ok = False

if all_ok:
    print("\nSUCCESS: All 15 routes resolved with HTTP 200 OK locally!")
else:
    print("\nFAILURE: Some routes returned error codes.")
