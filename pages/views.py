from django.shortcuts import render, get_object_or_404
from .models import (
    SiteSetting, CarouselSlide, ExecutiveMember, PastBearer,
    EditorialBoardMember, PublicationBook, ConferenceEvent,
    SocietyAward, JournalVolume, JournalArticle
)

def get_common_context():
    return {
        'site_settings': SiteSetting.objects.first(),
    }

def home(request):
    context = get_common_context()
    context['slides'] = CarouselSlide.objects.filter(is_active=True)
    return render(request, 'pages/home.html', context)

def about(request):
    context = get_common_context()
    return render(request, 'pages/about.html', context)

def executive_council(request):
    context = get_common_context()
    context['council_members'] = ExecutiveMember.objects.all()
    return render(request, 'pages/executive_council.html', context)

def legends(request):
    context = get_common_context()
    context['past_presidents'] = PastBearer.objects.filter(role='president')
    context['past_secretaries'] = PastBearer.objects.filter(role='secretary')
    context['past_treasurers'] = PastBearer.objects.filter(role='treasurer')
    context['past_editors'] = PastBearer.objects.filter(role='editor')
    return render(request, 'pages/legends.html', context)

def journal_current(request):
    context = get_common_context()
    # Vol 54 (2026) Issues 1 & 2
    context['issue_1_articles'] = JournalArticle.objects.filter(volume=54, issue=1)
    context['issue_2_articles'] = JournalArticle.objects.filter(volume=54, issue=2)
    return render(request, 'pages/journal_current.html', context)

def journal_archives(request):
    context = get_common_context()
    # Back archives Vol 42 (2014) to Vol 53 (2025)
    context['back_volumes'] = JournalVolume.objects.filter(volume_number__lt=54)
    return render(request, 'pages/journal_archives.html', context)

def editorial_board(request):
    context = get_common_context()
    context['board_members'] = EditorialBoardMember.objects.all()
    return render(request, 'pages/editorial_board.html', context)

def author_guidelines(request):
    context = get_common_context()
    return render(request, 'pages/author_guidelines.html', context)

def books(request):
    context = get_common_context()
    context['books_list'] = PublicationBook.objects.all()
    return render(request, 'pages/books.html', context)

def membership_info(request):
    context = get_common_context()
    return render(request, 'pages/membership_info.html', context)

def membership_directory(request):
    context = get_common_context()
    return render(request, 'pages/membership_directory.html', context)

def awards(request):
    context = get_common_context()
    context['awards_list'] = SocietyAward.objects.all()
    return render(request, 'pages/awards.html', context)

def awards_nomination(request):
    context = get_common_context()
    return render(request, 'pages/awards_nomination.html', context)

def conferences(request):
    context = get_common_context()
    context['events_list'] = ConferenceEvent.objects.all()
    return render(request, 'pages/conferences.html', context)

def election(request):
    context = get_common_context()
    return render(request, 'pages/election.html', context)

def register(request):
    context = get_common_context()
    return render(request, 'pages/register.html', context)

def login_view(request):
    context = get_common_context()
    return render(request, 'pages/login.html', context)

def search_view(request):
    query = request.GET.get('q', '').strip().lower()
    if not query:
        return render(request, 'pages/home.html', get_common_context())
    if any(w in query for w in ['journal', 'volume', 'issue', 'article', 'paper', 'current']):
        return render(request, 'pages/journal_current.html', get_common_context())
    elif any(w in query for w in ['archive', 'past issue', 'back volume']):
        return render(request, 'pages/journal_archives.html', get_common_context())
    elif any(w in query for w in ['editorial', 'board', 'editor', 'reviewer']):
        return render(request, 'pages/editorial_board.html', get_common_context())
    elif any(w in query for w in ['guideline', 'author', 'manuscript', 'submission', 'format']):
        return render(request, 'pages/author_guidelines.html', get_common_context())
    elif any(w in query for w in ['book', 'monograph', 'special publication']):
        return render(request, 'pages/books.html', get_common_context())
    elif any(w in query for w in ['fee', 'membership info', 'subscription', 'student fee', 'life member']):
        return render(request, 'pages/membership_info.html', get_common_context())
    elif any(w in query for w in ['directory', 'member list', 'fellow list']):
        return render(request, 'pages/membership_directory.html', get_common_context())
    elif any(w in query for w in ['register', 'registration', 'join']):
        return render(request, 'pages/register.html', get_common_context())
    elif any(w in query for w in ['login', 'signin', 'portal']):
        return render(request, 'pages/login.html', get_common_context())
    elif any(w in query for w in ['award', 'honor', 'medal', 'prasada', 'dodla', 'sarada', 'fppai']):
        return render(request, 'pages/awards.html', get_common_context())
    elif any(w in query for w in ['nomination', 'nominate']):
        return render(request, 'pages/awards_nomination.html', get_common_context())
    elif any(w in query for w in ['conference', 'seminar', 'symposi', 'workshop', 'event']):
        return render(request, 'pages/conferences.html', get_common_context())
    elif any(w in query for w in ['election', 'council election', 'vote']):
        return render(request, 'pages/election.html', get_common_context())
    elif any(w in query for w in ['council', 'executive', 'president', 'secretary', 'treasurer']):
        return render(request, 'pages/executive_council.html', get_common_context())
    elif any(w in query for w in ['legend', 'past president', 'past secretary', 'founder', 'nirula']):
        return render(request, 'pages/legends.html', get_common_context())
    else:
        return render(request, 'pages/about.html', get_common_context())

def contact(request):
    context = get_common_context()
    return render(request, 'pages/contact.html', context)
