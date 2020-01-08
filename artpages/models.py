from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
class Artwork(models.Model):
    PHOTO = 'photo'
    CHARECTER_DESIGN = 'charecter_design'
    VISUAL_DESIGN = 'visual_design'
    CARTOON = 'cartoon'
    FINE_ART = 'fine_art'
    ART_STYLES_CHOICES = [
        (PHOTO, 'Photo'),
        (CHARECTER_DESIGN, 'Charecter Design'),
        (VISUAL_DESIGN, 'Visual Design'),
        (CARTOON, 'Cartoon'),
        (FINE_ART, 'Fine Art')
    ]

    title = models.CharField(max_length=100, unique=True)

    short_desc = models.CharField(max_length=100, 
                                  help_text='A quick short description of the Artwork')

    desc = models.CharField(max_length=5000,
                                  help_text="A longer more indepth description of the ArtWork")

    image = models.ImageField(upload_to="gallery")

    slug = models.CharField(max_length=100, blank=True, editable=False)

    tag = models.CharField(max_length=32, choices=ART_STYLES_CHOICES)

    time_posted = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        path_components = {'name': 'Max', 'slug': self.slug}
        return reverse('', kwargs=path_components)

    def save(self, *args, **kwargs):
        if not self.pk:  # To detect new objects, check if self.pk exists.
            self.slug = slugify(self.title, allow_unicode=True)

        # Call save on the superclass.
        return super(Artwork, self).save(*args, **kwargs)


class Artist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.CharField(max_length=50000)
    major = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def save(self, *args, **kwargs):
        return super(Artist, self).save(*args, **kwargs)