from django.shortcuts import render, get_object_or_404
from django.conf import settings
from .models import Profile, Education, Skill, Project

def home(request):
    profile = Profile.objects.first()
    if not profile:
        # Fallback from settings
        c = settings.PORTFOLIO_CONTACT
        class Obj: pass
        profile = Obj()
        for k, v in c.items():
            setattr(profile, k, v)
    educations = Education.objects.all().order_by('-end_year', '-start_year')
    # Group skills by category
    skills = {}
    for s in Skill.objects.all().order_by('category', 'name'):
        skills.setdefault(s.category, []).append(s)
    projects = Project.objects.all().order_by('order', 'title')
    return render(request, 'portfolio/home.html', {
        'profile': profile,
        'educations': educations,
        'skills': skills,
        'projects': projects,
    })

def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/project_detail.html', {'project': project})