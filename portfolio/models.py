from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=120)
    tagline = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=40, blank=True)
    location = models.CharField(max_length=120, blank=True)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)
    about = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    start_year = models.IntegerField(null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)
    cgpa = models.CharField(max_length=20, blank=True)
    details = models.TextField(blank=True)

    def __str__(self):
        return f"{self.degree} – {self.institution}"

class Skill(models.Model):
    category = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    level = models.CharField(max_length=60, blank=True)  # e.g., Beginner/Intermediate/Advanced

    def __str__(self):
        return f"{self.name} ({self.category})"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.TextField(blank=True)  # comma-separated or paragraph
    github_url = models.URLField(blank=True)
    demo_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title