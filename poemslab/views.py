from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def nitin_auluck(request):
    return render(request, 'nitin_auluck.html')

def members(request):
    return render(request, 'members.html')

def research(request):
    return render(request, 'research.html')

def publications(request):
    return render(request, 'publications.html')

def opportunities(request):
    return render(request, 'opportunities.html')

def news_events(request):
    return render(request, 'news_events.html')

def resources(request):
    return render(request, 'resources.html')

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    return render(request, 'gallery.html')

def alumni(request):
    return render(request, 'alumni.html')